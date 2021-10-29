# -*- coding: utf-8 -*-

import random 
import os.path

nickname = [] # 이름 기록 리스트 
score = [] # 점수 기록 리스트

def rand(): 
    num = random.randrange(1, 101)
    return num

def put(a): # 최고기록을 파일에 저장하는 함수
    f=open("up_and_down.txt", 'a')
    history = name+' '+str(a)+'\n' #파일 내용 구분의 기준이 되는 개행문자
    f.write(history)
    f.close()

def read():
    score.clear()
    f=open("/Users/b/Desktop/up_and_down.txt", 'r') # 파일에서 읽어오기 r
    line=f.readlines() # 문자열로 불러와서 lines에 담기
    for i in range(0, len(line)):
        linesplit=line[i].split(' ') # 띄어쓰기를 기준으로 이름과 점수 나누기
        num = int(linesplit[1])
        score.append(num) 
        score.sort()
    f.close()

print("UP & DOWN 게임에 오신 걸 환영합니다~")
if not os.path.isfile('UP_and_down.txt'):     #-----> 피드백 1
    print("Up & Down 게임 기록을 위한 파일을 생성합니다.")
    f = open("up_and_down.txt", "w")
    f.close()
    
else:
    read()
while 1:
    print("\n1. 게임시작 2. 기록확인 3. 게임종료")
    menu = int(input('>> '))
    ans = rand() # 랜덤으로 1~100까지 정수를 하나 반환
    first = 1 # 범위 중 가장 작은 수
    last = 100 # 범위 중 가장 큰 수
    count = 1 #사용자가 숫자 맞추기에 도전한 횟수

    if menu == 1 : # 게임시작
        try:
          while True:
            if count==11:
              raise StopIteration
            user=int(input('%d번째 숫자 입력(%d~%d)>>'%(count, first, last))) # 사용자가 숫자 입력한 값 user
            if user > ans and user <= last:  # 사용자가 입력한 값이 정답보다 크고 범위중 가장 큰 수 보다 작을 때
                count += 1 # 도전 수 1추가
                print("DOWN") 
                last = user # 범위의 마지막수가 사용자가 입력한 값으로 바뀜
            elif user < ans and user >= first: # 사용자가 입력한 값: 가장 작은 수 < 입력한 값 < 정답
                count += 1 # 도전 수 1 추가
                print("UP")
                first = user # 범위 중 가장 작은 수가 사용자가 입력한 값으로 바꿈
            elif user > last or user < first: # 범위를 벗어나는 수를 입력 
              print("%d~%d 범위 안에 있는 수를 입력해주세요."%(first,last)) # 도전 수가 올라가지는 않음
            elif user == ans: # 정답 맞춤
                print('정답입니다!!')
                print('%d번째만에 맞추셨습니다' %count) # 몇 번째로 맞췄는지 count로 알려줌
                if not score:
                    print("최고기록 갱신~!\n")
                    name=input('닉네임을 입력하세요 >> ') 
                    put(count) 
                    score.append(count) # 점수 리스트에 점수 추가
                    nickname.append(name) # 이름 리스트 맨 앞에 이름 추가
                    score.sort() # 오름차순 정렬
                    break  
                elif count < score[0]: # 1등 기록인 score[0]보다 작으면 최고 점수
                    print("최고기록 갱신~!\n")
                    name=input('닉네임을 입력하세요 >> ') 
                    put(count)
                    score.append(count) # 점수 리스트에 점수 추가
                    nickname.insert(0, name) # 이름 리스트 맨 앞에 이름 추가
                    score.sort() # 오름차순으로 정렬

                    break
                else :
                    break
        except StopIteration:
          print("error : 입력횟수를 초과했습니다. 게임오버!")

    elif menu == 2 : # 기록확인
        result=[]
        f=open("/Users/b/Desktop/up_and_down.txt", 'r') # 파일에서 읽어오기 r
        lines=f.read() # 문자열로 불러와서 lines에 담기
        if lines: # 파일에 저장된 내용이 있을 경우
            result=lines.split('\n') #개행 문자를 기준으로 해서 파일의 내용 분리

            for i in range(len(result)-1, 0, -1): #파일의 최신 내용부터 출력
                print(len(result)-i, result[i-1])
        
        else : # 읽어온 데이터가 없을 경우
            print("아직 기록이 없습니다.")

        f.close()
    
    elif menu == 3 : # 게임종료
        print("게임을 종료합니다")
        break
    else : 
        print('잘못 입력하셨습니다. 1~3 중에서 다시 입력해주세요') # 사용자가 메뉴에 있는 1,2,3이 아닌 다른 수를 입력했을 때
