word="hEllo eveRyone"


print(word.upper())
print(word.lower())
print(word.swapcase())  #서로 바꾸기
print(word.title())

word1 = 'hello'
word2 = '12345'
word3 = " "

print(word1.islower())
print(word1.isupper())
print(word2.isdigit())
print(word3.isspace())

a = "HeLLLLLlo"

print(a.count('L')) #L 몇개 있는지
print(a.find('H'))
#H의 인덱스 위치 ('H', 0, 3) 인덱스 0~3까지 찾음, 공백도 인식, 못찾으면 -1 반환
print(a.rfind('H')) #오른쪽부터 찾기


#중요
word ="     나는 공부가 너무 재미있어서 공부가 공부만 하고 싶어요"

print(word)
print(word.strip()) #양쪽의 띄어쓰기 제거
print(word.rstrip('요'))
print(word.lstrip())

print(word.replace('공부','운동')) #공부 -> 운동

print(word.split()) # 띄어쓰기로 분리
print(word.split('가')) #'가'로 분리

data = ['A', 'B', 'C', 'D', 'E']

data_join = ''.join(data) # 문자열로 변환
print(data_join)

data2 = "1 2 3 4 5" # 공백이 포함된 문자열의 숫자 개수 찾기
d = data2.split()
print(len(d)) #띄어쓰기로 분리해서 개수구하기
print(len(data2.split()))

b = "20210811-312312"
print(b.split('-')[1][0]) #-로 구분하고 구분한거 2번째중에 인덱스0 문자
print(b.split('-'))
c = []
for i in b:
    c.append(i)
print(c)
