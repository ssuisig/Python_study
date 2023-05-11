import os
#os에서 제공하는 기능 사용


#파일 열 떄 오류 처리
#파일이 있는 줄 알고 짰는데 없음  -> 예외처리
dir_name = "/mnt/disk/"
name = "xxx.txt"
fullname = dir_name + name # 이경로 파일이 존재?
if not os.path.isdir(dir_name): # 존재하는지 확인 가능
    os.makedirs(dir_name) #없다면 만들기

if os.path.exists(name): #path에 name이 있으면
    f = open(name, "r")

    lines = f.readlines()

    f.close()
else: print("file 없음")


####파일 읽기

f = open("score.txt", "r") #r: 파일 읽기용

# readlines()
lines = f.readlines() #모든 줄 다 읽음

print(lines)
a=[]
sum = 0
avg = 0.0
for line in lines: #리스트, 딕셔너리, 문자열
    sum += int(line.strip())
    a.append(line.strip())
    #print(line.strip()) #줄바꿈 제거
avg = sum /len(lines)
print(avg)
print(a)

# f.close() #파일 닫기 중요!

#readline()
f = open("score.txt", "r")

while True:
    line = f.readline()
    if not line: #if line="";
        break
    print(line.strip())

f.close()

#read()
f = open("score.txt", "r")
data = f.read() #줄바꿈 포함 50줄이 하나의 문자열

print(data)



###파일 쓰기
x = "python"

f = open("fileWrite.txt","w") #파일이 생성되고 이미 있다면 덮어씌워짐

#write()
for i in range(1, 4):
    f.write(str(i)+'\n') #문자열만 가능

f.close()


f = open("result.txt", "w")

for i in range(1,11):
    data = '%d번째 줄\n'%i
    f.write(data)
f.close()

#with~as(close() 안하기)
with open("withAs.txt", "w") as f: #r도 가능
    f.write("withAs")


#예제1
f = open("star.txt",'w')

i = 7
while i > 0:
    f.write('*'*i + '\n')
    i -= 2

f.close()

#a: 이어쓰기
f = open("star.txt",'a')
f.write("append")
f.close()

#예제2
str = input("학번을 입력하세요:")

f = open("id.txt", 'w')
f.write(str)
f.close()

with open("id.txt", 'w') as f:
    f.write(str)

#예제3
f = open('id.txt', 'a')
f.write("\n전수연")
f.close()

#예제4
f = open('score.txt', 'r')
sum = 0
avg =0.0

lines = f.readlines()
for line in lines:
    sum += int(line)

avg = sum / len(lines)
print(avg)

f.close()

#예제5
f = open('score2.txt', 'r')
sum = 0
avg = 0.0

lines = f.readline()
linesList = lines.split(',')
for line in linesList:
    sum += int(line)

avg = sum / len(linesList)
print(avg)

f.close()
