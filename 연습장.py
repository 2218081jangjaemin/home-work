import time
import datetime

#(반복문) 종료 번호(4번)가 나올때까지 반복
#(함수, 사용자 입력 함수) input, print 등
#(조건문) if, while 등
#datetime , time 함수로 날짜 불러오고 계산하도록 설정
#복무일은 육군(546일)을 기준으로 한다.

MODE=0
while(MODE!=3):
    X=0
    Y=0
    RESULT=0
    MODE_2=0
    print("========================")
    print("  복무율 계산기  ")
    print("     제작 : 장재민    ")
    print("1 - 나의 제대는 언제?")
    print("2 - 나는 몇퍼센트 했지?")
    print("3 - 종료")
    print("=======================")
    MODE=int(input("어떤 것을 이용하시겠어요? : "))
    if (MODE==1):
        #print("입대일을 입력해주세요. (예: 2023-02-20) : ")
        print("내 제대는 언제?")
        GET=input("입대일을 입력해주세요. (예: 2023-02-20) : ").split('-')
        DATE=datetime.date(int(GET[0]),int(GET[1]),int(GET[2]))
        print("제대일 : ",DATE+datetime.timedelta(days=546))
    if (MODE==2):
        print("나는 몇퍼센트 했지?")
        TODAY = datetime.date.today()
        GET=input("입대일을 입력해주세요. (예: 2023-02-20) : ").split('-')
        DATE=datetime.date(int(GET[0]),int(GET[1]),int(GET[2]))
        DDAY = TODAY-DATE
        #현재 복무율을 소수 2번째 자리까지 표시한다.
        print(f"현재 복무율 : {round((DDAY.days/546)*100,2)}%")
        LEFT = round((DDAY.days/546)*10)
        #만약 1보다 작을경우 마이너스로 넘어가지 않도록 세팅
        if (LEFT<1):
            LEFT=1
        #100% 보다 클경우 초과하지 않도록 세팅
        if (LEFT>9):
            LEFT=10
        #복무율을 네모 그래프로 나타낸다.
        print("[ ",end="")
        for i in range (LEFT):
            print("■",end="")
        for j in range (10-LEFT):
            print("□",end="")
        print(" ]")
    if (MODE==3):
        print("짝짝짝. 종료되었습니다.")
