import RPi.GPIO as GPIO #gpio 라이브러리 호출
import time #시간함수 호출
import random as rd #랜덤함수 호출

GPIO.setmode(GPIO.BCM) #bcm 모드를 사용하여 점등될 led의 번호 입력
GPIO.setup(26,GPIO.OUT) 
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT) #각 핀들을 아웃핏 모드로 초기화

while True:
    try:
        GPIO.output(26,GPIO.HIGH) #점등
        time.sleep(1.0)     #1초 대기
        GPIO.output(26,GPIO.LOW) #소등
        time.sleep(1.0) # 1초 대기
        GPIO.output(16,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(16,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(21,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(20,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(20,GPIO.LOW) # 각 다른 핀들도 위와 동일 
        time.sleep(1.0)
        
    except:  
        GPIO.cleanup()  # 컨트롤 c 가 입력되면 gpio를 모두 클리어
        print('end')
        break
        
    