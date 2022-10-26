import RPi.GPIO as GPIO #gpio 라이브러리 호출
import time #시간함수 호출
import random as rd #랜덤함수 호출
list = [16,20,21,26] #각 핀의 번호를 리스트로 생성

GPIO.setmode(GPIO.BCM) #bcm 모드를 사용하여 점등될 led의 번호 입력
GPIO.setup(26,GPIO.OUT) 
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT) #각 핀들을 아웃핏 모드로 초기화

for i in range(10):  #10번의 동작
    number =rd.choice(list) #리스트에서 무작위의 번호를 하나 추출하여 저장
    GPIO.output(number,GPIO.HIGH) #추출된 번호의 핀에 점등
    time.sleep(0.5) #0.5초 대기
    GPIO.output(number,GPIO.LOW) #추출된 번호의 핀 LED 소등
    time.sleep(0.5) #0.5초 대기
 
GPIO.cleanup() # gpio 초기화


    