import urllib.request
from bs4 import BeautifulSoup

#사이트에서 html형식으로 리소스를 읽어오기
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

#각 학과의 링크 a만 추출하기
department = soup.findAll("a")

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과\t\t\t\t홈페이지")

for s in department:
   
   # 학과, 전공 이외의 것들은 제외
    if s.text =="자율전공학부" or s.text =="공동기기실":
            continue
    if "대학원" in s.text:
            continue
        
    # 학과, 전공일 경우 읽어오기
    else:   
        htmlDeeper= urllib.request.urlopen("http://www.swu.ac.kr"+s['href'])    
        result2= BeautifulSoup(htmlDeeper.read(),"html.parser")         
        major = result2.find("a",{"class","btn btn_xl btn_blue_gray"}) 
      
        print(s.text,end='') #학과 이름 출력
        # 홈페이지가 없는 학과의 경우
        if major is None : 
            print("\t\t홈페이지가 존재하지 않음")
        else:
            if "홈페이지" in major.text:    
                print("\t\t\t"+major['href'])
            else :   
                print("\t\t\t홈페이지가 존재하지 않음")
