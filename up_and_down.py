import random 

score = [] # 점수 기록
menu =0 #메뉴의 디폴트 값

def rand(): # rand함수 (컴퓨터 1부터 100까지 수 중에서 하나를 랜덤으로 골라주고 리턴해줌)
    num = random.randrange(1, 101)
    return num

while 1:
    print("UP & DOWN 게임에 오신 걸 환영합니다~")
    print("\n1. 게임시작 2. 기록확인 3. 게임종료")
    menu = int(input('>> '))
    ans = rand() # 랜덤하게 1~100까지 하나의 정수를 반환함
    first = 1 # 범위 중 가장 작은 수
    last = 100 # 범위 중 가장 큰 수
    count =1 #사용자가 숫자 맞추기에 도전한 횟수
    
    if menu == 1 : # 게임시작
      
      while(count<=11):
        if count ==11:
          print("10번을 초과하여 숫자를 입력했습니다. 게임을 종료합니다.")
          break
        user=int(input('%d번째 숫자 입력(%d~%d)>>'%(count, first, last))) # 사용자가 숫자 입력한 값 user
        if user > ans and user <= last: # 사용자가 입력한 값이 정답보다 크고 범위중 가장 큰 수 보다 작을 때
            count += 1 # 도전 수 1추가
            print("DOWN") 
            last = user # 범위의 마지막을 사용자가 입력한 값으로 바꿈
        elif user < ans and user >= first: # 사용자가 입력한 값: 가장 작은 수 < 입력한 값 < 정답
            count += 1 # 도전 수 +1
            print("UP")
            first = user # 범위 중 가장 작은 수가 사용자가 입력한 값으로 바꿈
        elif user > last or user < first: # 범위를 벗어나는 수를 입력 
            print("1~100 범위 안에 있는 수를 입력해주세요.") # 도전 수가 올라가지는 않음
        elif user == ans: # 정답 맞춤
            print('정답입니다!!')
            print('%d번째만에 맞추셨습니다' %count) # 몇 번째로 맞췄는지 count로 알려줌
            if not score:
                print("최고기록 갱신~!\n") 
                score.append(count) # 점수 리스트에 점수 추가
                score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                break  
            elif count < score[0]: # 1등 기록인 score[0]보다 작으면 최고 점수
                print("최고기록 갱신~!\n")
                score.append(count) # 점수 리스트에 점수 추가
                score.sort() # 리스트 오름차순으로 정렬해놓기(가장 작은수가 앞에 오므로 자동으로 1등이 score[0]이다.)
                break
            else : # 최고기록 갱신을 하지 않았을때는 아무것도 기록하지 않음
                break
                    
    elif menu == 2 : # 기록확인
        score.sort()
        for index, value in enumerate(score):
          print(index+1, value)
   
    
    elif menu == 3 : # 게임종료
        print("게임을 종료합니다")
        break
    else : 
        print('잘못 입력하셨습니다. 1~3 중에서 다시 입력해주세요') # 사용자가 메뉴에 있는 1,2,3이 아닌 다른 수를 입력했을 때
