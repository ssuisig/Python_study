score = [1, 2, 3, 4, "hi"]
print(score)  # == print(score[:])
print(score[1])
print(score[4])
print(score[2:])  # 2부터 다 출력
print(score[:-2])
print(score[::-2])

numList = []
# 배열 뒤에 추가
numList.append('alpha')
numList.append('bravo')
# 정해진 자리에 추가(사이)
numList.insert(1, 'hi')

print(numList)

# for 문으로 배열 추가
x = []
for i in range(1, 11):
    x.append(i)
print(x)

y = []
for i in range(1, 11):
    y.append(x[10 - i])
print(y)

# 배열 값 덮어쓰기
x[2] = 0
print(x)

# 값 지우기(중복된 값이라면 처음 것)
x.remove(0)

# 뒤에서부터 값을 뽑아 삭제
print(x.pop())
print(x)

# 리스트의 전체 항목 개수
print(len(x))

# len()을 이용한 총합과 평균 구하기
sum = 0
avg = 0.0
for i in range(len(x)):
    sum += x[i]
avg = sum / len(x)
print(sum, avg)

# 리스트 정렬-> 원래 리스트의 순서 자체가 바뀜
a = [1, 5, 11, -5, 3]
a.sort()  # (reverse = False): 오름차순, default / (reverse = True): 내림차순
print(a)

# reverse() -> 자기자신의 리스트만 바꿀 수 있음
a.reverse()
print(a)
# 다른 리스트에 역순으로 저장하고 싶다면
ar = a.copy()
ar.reverse()
print(ar)

# 리스트 복사
b = a.copy()
print(b)

# 키 값 찾기
print(a.count(11))

# 예제1
greetings = ['안녕', '니하오', '하이', '곤니찌와']

for i in range(len(greetings)):
    print(greetings[i])

# 예제2
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'hotel', 'india']
b = []
for i in a: # for i in a -> 배열 이름을 써주면 배열의 크기 만큼 반복
    if len(i) == 5: # a[i]가 아니라 i써주면 됨, i에 배열 원소가 하나씩 들어감
        b.append(i)
print(b)
