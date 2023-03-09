# 주석: #,ctrl+k+c 주석 풀기 ctrl+k+u,,,파이참은 ctrl+/
#단어완성 단축키 tab
#print('hello')

print("안녕하세요")
print('여러분 %s 나는 %d살입니다.'%("hello", 30))

x = 1
y = 2
z = x+y
print("%d+%d는 %d입니다."%(x, y, z))

x = 1.1234
y = 2.4567
print("%d"%(x+y))
print("%f"%(x+y))
print("%c" %"c")

# 이스케이프 문자
print("안녕하세요.\n\t하이")
print("\', \", \\")

#데이터형
x = True
y = False
a = 1.4
b = "data"
print(type(b))

#정수, 실수 같이 덧셈-> type 실수, 정수, 정수 나누기-> 실수(예외)
x = 5
y = 10
print(y/x)

a = "data science"
b = '데이터 사이언스'
print(a, b)
x = "동덕 "+"여대"+'데이터'+' 사이언스'
print(x)

t = 'hi'
print(t*3)

x = 100 > 10 #위에 같은 이름 변수 가장 최근 껄로 덮어 씀
y = (2 == 1)
print(x)
print(y)

#변수 이름 대소문자 구분, 영문 숫자만 사용 가능 단, 영문부터 시작
# (_: 띄어쓰기 대신 사용)
#print = 10 가능하지만 print기능 못쓰게 됨

#input 함수로 입력받는 데이터는 모두 문자열로 인식
#x = input("숫자 하나만 입력해주세요: ")
#print(x)
#print(x+3)-> x를 문자열로 인식해서 오류남
# int(), float(), str()
# print(int(x)+3)
# name = input("당신의 이름을 입력해주세요: ")
# print("당신의 이름은 %s 입니다."%name)


# a = 3
# b = str(a)
# print(b*3)
# name = input("이름을 입력해주세요: ")
# std_num = input("학번을 입력해주세요: ")
# print("이름: %s 학번: %s"%(name, std_num))
# print("이름: ", name,"학번: ", std_num)

#몫 구하기
print(5//3)
print(5/3)
#나머지 값
print(5%3)
#제곱
print(5**3)

#복합 대입 연산자
a = 90
a = a//3
a //= 3

# a = input("나눠지는 수 ==> ")
# b = input("나누는 수 ==> ")
# c = int(a) // int(b)
# d = int(a) % int(b)
# print(a, "을(를)", b, "(으)로 나눈 몫은", c, "입니다.")
# print(a, "을(를)", b, "(으)로 나눈 나머지는", d, "입니다.")

#더 짧게
#a = int(input("나눠지는 수 ==> "))
#b = int(input("나누는 수 ==> "))
# print(a, "을(를)", b, "(으)로 나눈 몫은", a//b, "입니다.")
# print(a, "을(를)", b, "(으)로 나눈 나머지는", a%b, "입니다.")

#비교 연산자
a = (100 != 10)
print(a)

# password = "2021"
# id = input("암호입력: ")
# print(password == id)

#논리 연산자
x = 1
y = 10

z = not(x > 0) and (y < 100)
print(z)
print(not(z))



