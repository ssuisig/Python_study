# 함수
num = '20210811-3234567'
def find_gender(x):
    if x.split('-')[1][0] == '3':
        print("male")
    elif x.split('-')[1][0] == '4':
        print("female")

find_gender(num)

# sum()만 해도 다 더해줌

a = [90, 80, 60]
def ssu(list):
    average = sum(list) / len(list)
    return average

result = ssu(a)
print(result)

#반환값이 없는 함수
def printD():
    print("printD")

printD()

#반환값이 여러개 있는 함수
x = 5
y = 1
z = 10
def sa(a, b, z = 10):
    sum = a + b + z
    diff= a - b +z
    return sum, diff

n, m = sa(x, y)
print(sa(x, y))
print("%d, %d"%(n, m))

#지역변수, 전역변수

def fun1():
    a = 10
    print(a)
def fun2():
    print(a)

a = 20
fun1() #지역변수 10
fun2() #전역변수 20

#예제1
def fun01(s):
    print(s)

fun01("hello")
#fun01() 에러-매개변수X

#예제2
def n_plus_1(n):
    result = n + 1

#n_plus_1(3) #반환값X
#print(result) #함수의 지역변수 사용

#예제3
def make_url(string):
    print("www."+string+".com")

make_url("naver")
make_url("facebook")

#예제4
def make_list(string):
    a = list(string)
    print(a)

make_list("naver")
make_list("facebook")

#예제5
def pickup_even(items):
    a = []
    for i in items:
        if i % 2 == 0:
            a.append(i)
    print(a)

pickup_even([3, 4, 5, 6, 7, 8])

#예제6
score = [80, 75, 91, 47, 66, 82, 57, 65, 90, 91, 33, 39, 78, 59]

def average(list):
    avg = sum(list) / len(list)
    return avg
print(average(score))
