import RPi.GPIO as GPIO
import time

SW =[5,6,13,19]  #bcm 모드 핀번호 입력
swValue =[0,0,0,0] #입력 받은 값을 저장
BUZZER = 12 #버저 출력 핀번호 설정
GPIO.setwarnings(False) #경고 무시
GPIO.setmode(GPIO.BCM) #bcm 모드로 설정
GPIO.setup(BUZZER,GPIO.OUT) #12번 핀을 버저 출력으로 사용
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 각 스위치를 입출력으로 사용
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
ryme = [262,294,330,349] #도레미파

p = GPIO.PWM(BUZZER,261) #진폭설정
p.start(50) #시작

p.stop() #소리가 나지 않게끔 설정

try:
    while True:
        for i in range(len(SW)): # SW리스트의 길이만큼 
            swValue[i] = GPIO.input(SW[i])   #value 값을 받아 저장        
            if swValue[i]==1: #입력이 들어오면
                p.start(50)
                p.ChangeFrequency(ryme[i]) #각 리스트의 입력된 계이름 출력
                time.sleep(0.3)
                p.stop()
                time.sleep(0.1)          
        time.sleep(0.1)
        
except KeyboardInterrupt: #ctrl+c 입력시 종료
    pass

GPIO.cleanup() 