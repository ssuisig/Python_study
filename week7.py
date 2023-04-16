a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'hotel', 'india']
b = []

for i in a:
    if len(i) == 5:
        b.append(i)
print(b)

# 튜플 - 읽기, 연산가능/ 수정, 추가X
x = (10, 20, 30)
# x[0] = 15 --> 오류
# x = (1) --> 그냥 int 1이 됨 x = (1,) 이렇게 써줘야 됨
print(x)
y = list(x)  # 튜플->리스트
x = tuple(y)  # 리스트->튜플
del x

# 딕셔너리 -> 키:값

x = {1: 'a', 2: 'b', 3: 'c'}
y = {'1교시': '파이썬', '2교시': '수학', '3교시': '영어'}

print(x)
print(y)

professor = {'학번': '20231234', '이름': '전수연', '부서': '컴퓨터학과'}
professor['나이'] = 22  # 키:값 추가
print(professor)
print(professor['이름'])

professor['부서'] = '데이터사이언스학과'  # 값 바꾸기 - 덮어쓰기
print(professor['부서'])

del (professor['나이'])  # 키:값 삭제
print(professor)

# 키 or 값만 읽기
print(professor.keys())
print(list(professor.keys()))

print(professor.get('부서'))  # print(professor['부서']) 같은 의미

print(professor.values())
print(list(professor.values()))

print('학번' in professor)  # 딕셔너리에 key가 있는지 boolean 반환

for i in professor:
    print(i, professor[i])
# 같은 코드
for i in professor.keys():
    print(i, professor[i])

# 키, 값 한번에 나오는 함수/가장 많이 씀 시험문제 다시쓰기
for k, v in professor.items():
    print(k, v)

print(list(professor.items()))

# 예제1
foods = {"떡볶이": "김밥", "자장면": "단무지", "라면": "파김치", "치킨": "맥주", "삼겹살": "소주"}

while True:
    food = input(str(list(foods.keys()))+"중 좋아하는 음식은? ")
    if food == '끝' or food not in foods:
        break
    print(food+ "궁합 음식은 "+ foods[food]+ " 입니다.")

# 예제2
scores = {'김예진':90, '박영진':95, '김소희': 84}
sum = 0

for key in scores:
    sum += scores[key]
    print('%s : %d' % (key, scores[key]))

avg = sum/len(scores)
print('합계 : %d, 평균 : %.2f'%(sum, avg))

# 예제3
words = {'사과':'apple', '컴퓨터':'computer', '학교':'school', '책상':'desk', '의자':'chair'}

for i in words.keys():
    word = input(i+"에 해당되는 영어 단어를 입력해주세요: ")
    if words[i] == word:
        print("정답입니다!")
    elif word == "끝" or word not in words: break
    else: print("틀렸습니다!")

