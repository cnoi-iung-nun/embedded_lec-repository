import RPi.GPIO as GPIO
import time

PWMA = 18 #속도 입력 
PWMB = 23 
AIN1 = 22 #  방향 입력
AIN2 = 27
BIN1 = 25
BIN2 = 24
SW =[5,6,13,19] #스위치 번호
swValue =[0,0,0,0] #스위치의 입력값을 저장
waysign =['sw1:go straight', 'sw2:turn Right', 'sw3:turn Left', 'sw4:go back']
GPIO.setwarnings(False)#경고 무시
GPIO.setmode(GPIO.BCM)#bcm 모드로 설정
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT) # 각 포트를 출력으로 사용
for i in range (4):
    GPIO.setup(SW[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)# 각 스위치를 입력으로 사용

L_Motor = GPIO.PWM(PWMA,500) #왼쪽 모터 제어
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500) #오른쪽 모터 제어
R_Motor.start(0)

def moving(x) : # 함수 선언하여 방향별 움직임을 구현
            if x==5: #1번 스위치
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1) # 직진하기 위한 바퀴 설정
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50) #바퀴  속도 설정           
            
            elif x== 6: #2번 스위치
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,1)
                GPIO.output(BIN2,0) #우회전을 위한 바퀴 설정
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
                
            elif x == 13: #3번 스위치
                GPIO.output(AIN1,1)
                GPIO.output(AIN2,0)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1) # 좌회전
                R_Motor.ChangeDutyCycle(50)
                L_Motor.ChangeDutyCycle(50)
                
            elif x == 19: #4번 스위치
                GPIO.output(AIN1,1)
                GPIO.output(AIN2,0)
                GPIO.output(BIN1,1)
                GPIO.output(BIN2,0) #후진
                L_Motor.ChangeDutyCycle(50)
                R_Motor.ChangeDutyCycle(50)
                

try:
    while True:
        for i in range(len(SW)): #각 스위치의 상태를 확인하며
            swValue[i] = GPIO.input(SW[i])  #입력이 들어왔을 경우 값을 swValue 리스트에 저장          
            if swValue[i]==1: #입력이 들어오면 
                print(waysign[i]) # 각 스위치의 방향에 맞는 문구 출력
                moving(SW[i]) # 움직이는 함수 호출
                while(GPIO.input(SW[i])==1): continue # 입력이 1인 경우 즉, 계속 누르고 있을 경우에만 동작
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)    # 입력이 없으면 바로 정지
       

except KeyboardInterrupt:
    pass

GPIO.cleanup()
