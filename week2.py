##파이썬 2주차

##if 조건문 :
x = 1
if x > 1:
    print("hello") #들여쓰기로 if문 진행사항 파악
print("hi")

#패스워드 확인하기
password = "data"
password2 = input("비밀번호를 입력해 주세요 : ")

if password == password2 :
    print("\"correct\"")

#if문에서 수행할 문장 pass하기
a = 3
b = 3
if a == b:
    pass


num = int(input("숫자를 입력해 주세요 :"))
if num % 2 == 0:
    print("입력하신 숫자는 짝수 입니다.")
if num % 2 == 1:
    print("입력하신 숫자는 홀수 입니다.")
if num < 0:
    print("0보다 큰 숫자를 입력해 주세요.")

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
if num < 0:
    print("0보다 큰수")

#줄여서 쓰기
message ="3보다 큼" if num > 3 else "3보다 작음"
print(message)

#if, else
x = 100
if x > 50:
    if x > 90:
        print("매우 크네요")
    else:
        print("90보단 작네요")
else:
    print("50보다 작네요")

score = 65
##큰 숫자부터 짜기
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

#elif
score = 77

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else: print("F")

#예제 1
str = input("고객님께서 사용 중이신 통신사를 입력해 주세요 : ")
if str == "SKT":
    print("고객님꼐서 사용 중이신 통신사는 SK 텔레콤 입니다.")
elif str == "KT":
    print("고객님꼐서 사용 중이신 통신사는 KT 입니다.")
elif str == "LG":
    print("고객님꼐서 사용 중이신 통신사는 LG U+ 입니다.")

#예제 2
age = int(input("고객님의 나이를 입력해 주세요: "))
if age >= 60: print("고객님의 연령대는 60대 이상 입니다.")
elif age >= 50: print("고개님의 연령대는 50대 입니다.")
elif age >= 40: print("고개님의 연령대는 40대 입니다.")
elif age >= 30: print("고개님의 연령대는 30대 입니다.")
elif age >= 20: print("고개님의 연령대는 20대 입니다.")
else: print("고개님의 연령대는 10대 입니다.")

#예제 3
num = int(input("자연수를 입력하여 주십시오 : "))
if num > 0:
    if num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
else:
    print("자연수가 아닙니다.")

#더 짧게
if age < 0 : print("0보다 큰 숫자 입력해")
elif age % 2 == 0: print("짝수")
else : print("홀수")

#예제 4
lank = input("회원 등급을 입력하세요 : ")
price = int(input("구매 금액을 입력하세요: "))
if lank == "S":
    print("할인된 가격:%d"%(price*0.95))
elif lank == "G":
    print("할인된 가격:%d"%(price*0.9))
elif lank == "V":
    print("할인된 가격:%d" % (price * 0.85))

#예제 4 풀이
net_price = 0

if lank == "V":
    net_price = price * 9.85
elif lank == "G":
    net_price = price *0.9
else : net_price = price

print("지불하실 금액은 %d"%net_price)

eng = int(input("영어시험 점수를 입력하세요 : "))
math = int(input("수학시험 점수를 입력하세요 : "))

#예제 5
if eng >= 80 and math >= 80:
    print("합격")
elif eng >= 80 or math >= 80: #이 조건을 else로
    print("재시험 기회제공")
elif eng < 80 and math < 80:
    print("불합격")

#예제 5 풀이
if eng >= 80 and math >= 80:
    print("합격")
elif eng < 80 and math < 80:
    print("불합격")
else:
    print("재시험 기회 제공")

#예제 6
age = int(input("나이를 입력하세요 : "))
fee = 0
if age <= 10: fee = 0
elif age < 65: fee = 1000

print("입장료는 %d원 입니다."%fee)



