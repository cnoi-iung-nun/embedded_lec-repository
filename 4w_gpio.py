import RPi.GPIO as GPIO #gpio 라이브러리 호출
import time #시간함수 호출


GPIO.setmode(GPIO.BOARD)  #board 모드를 사용하여 점등될 led의 핀번호 입력
GPIO.setup(37,GPIO.OUT) #gpi 26
GPIO.setup(36,GPIO.OUT) #36 gpi16
GPIO.setup(40,GPIO.OUT) #40 gpi21
GPIO.setup(38,GPIO.OUT) #38 gpi20 각핀들을 아웃핏 모드로 초기화

while True:
 
        GPIO.output(37,GPIO.HIGH) #37번 보드번호 점등
        time.sleep(1.0)    #1초 대기
        GPIO.output(37,GPIO.LOW) #37번 보드번호 소등
        time.sleep(1.0)  #1초 대기
        GPIO.output(36,GPIO.HIGH) #36번 보드 번호 소등
        time.sleep(1.0)     #1초 대기 
        GPIO.output(36,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(40,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(40,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(38,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(38,GPIO.LOW)
        time.sleep(1.0)
 
    