import threading
import serial
import time
import RPi.GPIO as GPIO

bleSerial =serial.Serial("/dev/ttyS0",baudrate=9600, timeout=0.1) #블루투스 시리얼 설정
PWMA, AIN1, AIN2 = 18, 22, 27
PWMB, BIN1, BIN2 = 23, 25, 24 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT)#출력포트로 사용
GPIO.setup(PWMB,GPIO.OUT)#출력포트로 사용
GPIO.setup(AIN1,GPIO.OUT)#출력포트로 사용
GPIO.setup(AIN2,GPIO.OUT)#출력포트로 사용
GPIO.setup(BIN1,GPIO.OUT)#출력포트로 사용
GPIO.setup(BIN2,GPIO.OUT)#출력포트로 사용
L_Motor = GPIO.PWM(PWMA,500) # 모터 초기 설정
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500) # 모터 초기 설정
R_Motor.start(0)
gData = ""  #전역변수 설정

def go() :         # 앞으로 이동
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    L_Motor.ChangeDutyCycle(50)
    R_Motor.ChangeDutyCycle(50)             
            
def right(): # 오른쪽으로 방향 전환
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    L_Motor.ChangeDutyCycle(50)
    R_Motor.ChangeDutyCycle(50)
                
def left(): # 왼쪽으로 방향 전환
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(50)
    L_Motor.ChangeDutyCycle(50)
                
def back(): # 뒤로 이동
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    L_Motor.ChangeDutyCycle(50)
    R_Motor.ChangeDutyCycle(50)

def stop(): # 정지
    L_Motor.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)

def serial_thread(): # 통신 쓰레드 함수 선언
    global gData
    while True:
        data = bleSerial.readline() # 읽고
        data = data.decode() # 디코딩 하여
        gData = data # 전역변수에 저장

def main():
    global gData 
    try:
        while True:
            if gData.find("go") >= 0: # go 입력시  앞으로 이동
                gData = "" # 전역변수 초기화
                print("ok go") 
                go()  # 앞으로 이동 함수 호출

            elif gData.find("back") >=0: #back 입력시  뒤로 이동
                gData = ""  # 전역변수 초기화
                print("ok back")
                back() # 뒤로 이동 함수 호출

            elif gData.find("left") >=0:
                gData = ""  # 전역변수 초기화
                print("ok left")
                left() #왼쪽으로 방향 전환 함수 호출

            elif gData.find("right") >=0:
                gData = ""  # 전역변수 초기화
                print("ok right")
                right() #오른쪽으로 방향 전환 함수 호출 

            elif gData.find("stop") >=0:
                gData = ""  # 전역변수 초기화
                print("ok stop")
                stop() # 멈춤 함수 호출

    except KeyboardInterrupt:
        pass        

if __name__ == "__main__":
    task1 =threading.Thread(target=serial_thread) # 타겟 쓰레드 호출
    task1.start() # 쓰레드 시작
    main() # 메인함수 호출 
    bleSerial.close() # 블루투스 시리얼 통신 종료
    # 커밋 파일 수정을 위한 테스트
