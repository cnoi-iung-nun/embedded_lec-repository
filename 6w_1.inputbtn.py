import RPi.GPIO as GPIO
import time

SW =[5,6,13,19] #bcm 모드 핀번호 입력
insw = [0,0,0,0] # 몇번 눌렸는지에 대한 값을 저장
swValue =[0,0,0,0]#입력 받은 값을 저장
GPIO.setwarnings(False)#경고 무시
GPIO.setmode(GPIO.BCM)#bcm 모드로 설정
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # 각 스위치를 입력으로 사용하며 눌렸는지 안눌렸는지 체크
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


try:
    while True:
        for i in range(len(SW)): #각 핀번호에 맞게
            swValue[i] = GPIO.input(SW[i]) #핀에 들어오는 값을 저장 
        for i in range(len(SW)): # 각 스위치를 확인하며
            if swValue[i]==1: #스위치가 눌렸을 경우
                insw[i] += 1 # 카운트 활성화 이때 0이 아닌 1로 출력 되게끔 함
                print("SW{} click,{}".format(i+1,insw[i]) ) # 몇번 스위치가 몇번 눌렸는지 출력
        time.sleep(0.1)
        
except KeyboardInterrupt: # ctrl+c 입력시 종료
    pass

GPIO.cleanup()