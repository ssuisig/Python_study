#반복문 for, while

#for----------------------------

# *
# **
# ***
# ****
for i in range(5):
    print("*"*i)



# 1~30 중 3의 배수만 출력
for i in range(1, 31, 1):
    if i % 3 == 0:
        print(i) #옆에 붙여 쓰는 건 어케하지
    else:
        print("X")

# 팩토리얼 값 구하기
num = int(input("2 이상의 숫자를 입력해 주세요:"))
result = 1
for i in range(1, num+1):
    result = result * i
print(result)

for i in range(1, num):
    num *= (num-i)
print(result)

# 10까지 합
sum = 0

for i in range(1, 11):
    sum += i
print(sum)

# 1000~2000 사이 홀수의 합
sum = 0

for i in range(1001, 2001): #(1001, 2001, 2)
    if i % 2 == 1:
        sum += i
print(sum)

# 구구단 구하기
num = int(input("몇 단?:"))
for i in range(1, 10):
    print("%d x %d = %d"%(num, i, num*i))

#중첩 for문
for i in range(3):
    for j in range(2):
        print(i,j,"안녕하세요")

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d"%(i, j, i*j))

#while-------------------------

i = 0
while i < 3:
    print("%d : 안녕하세요"%i)
    i += 1

# 1~10까지 합
i = 1
sum = 0
while i < 11:
    sum += i
    i += 1
print(sum)

# * 출력
i = 0
while i < 5:
    print("*"*10)
    i += 1

# 반복문 탈출 break
while True:
    print("hi")
    break

# 1~10까지 합에서 최초로 40을 넘는 숫자
i = 1
sum = 0
while i < 11:
    sum += i
    if sum > 40: break
    i += 1
print(sum)

# 반복문의 처음으로 돌아가게 하는 continue
for i in range(10):
    if i % 3 == 0:
        continue
    print(i) # 조건을 만족하면 밑을 수행하지 않고 처음으로 돌아감

#예제 1
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

sum = 0
i = 1
while i < 101:
    sum += i
    i += 1
print(sum)

#예제 2
money = 1000
year = 0
while money < 2000:
    money += money*0.07
    year += 1
print(year,"년")

#예제 3
i = 1
result = 0
while 30 >= i:
    if 30 % i == 0 and 75 % i == 0:
        result = i
    i += 1
print(result)

i = 1
result = 0
for i in range(31, 1, -1):
    if 30 % i == 0 and 60 % i == 0:
        result = i
        break
print(result)