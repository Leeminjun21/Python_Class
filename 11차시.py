# f = open("C:/미래모빌리티공학과/MinJun LEE/python/newfile2.txt", 'x')
# f.close()

# f = open('ex_memo.txt', 'w')
# students = ['이민준', '윤동현', '혜원 진', '깅지원']
# for student in students:
#     msg = student
#     f.write(msg+"\n")
# f.close()


# file = open('hello.txt', 'wt')   # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 변환
# file.write('미국 거지가 한국천재보다 영어를 잘한다.')      # 파일에 문자열 저장
# file.close()

# a: 쓰기
# f = open('test.txt', 'a', encoding='UTF-8')

# for i in range(4,10):
#     data = "%d 번째 줄입니다. \n"%i
#     f.write(data)
# f.close()

# dict1 = {'hello' : 1, 'brother' : 2}
# file1 = open("Original.txt", "w")

# str1 = repr(dict1)
# file1.write("dict1 = " + str1 + "\n")

# file1.close()

# test_file = open("test2.txt","w")

# a = 23
# b = 58
# test_file.write('%d + %d = %d' %(a, b, a+b)+'\n')
# test_file.write('%d - %d = %d' %(a, b, a-b))
# test_file.close

# from random import randint # 난수 생성 랜덤 int를 가져옴

# with open('text3.txt', 'w') as f:
#     f.write('이번주 로또 번호는 ->')
#     for lotto in range(6):
#         f.write(str(randint(0,50)) +', ')

# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'w') as file:
# # hello.txt 파일을 쓰기 모드(w)로 열기
#     file.writelines(lines)
# file.close()

# w: 쓰기
# f= open('ex_memo1.txt', 'w')
# students = ['이민준', '윤동현', '혜원 진', '깅지원']
# for student in students:
#     msg = student
#     f.write(msg+' ')
# f.close()

# f= open('ex_memo1.txt', 'w')
# students = ['이민준', '윤동현', '혜원 진', '깅지원']
# f.writelines("\n".join(students))
# f.close()

# 파일 r 모드로 열기
#f = open('t2.txt', 'r')

# read() 함수 이용해서 하나씩 읽어오기
# print('\n1. read()')
# print(f'위치 : {f.tell()}')
# s1 = f.read(2)
# print(s1)


# readline() 함수 이용해서 한 라인씩 읽어오기
# print('\n2.readline()')
# print(f'위치 : {f.tell()}')

# s2 = f.readline()
# print(s2)

# s2 = f.readline()
# print(s2)

f = open('test.txt', 'r', encoding='UTF-8')
line = f.readline()  # 파일의 라인 끝에 줄 바꿈 (\n) 이 있을 경우 줄 바꿈을 포함합니다.
line = line.strip()  # 줄 빠굼 (\n) 제거
print(line) # 1번째 줄입니다.
line = f.readline()
line = line.strip()
print(line) # 2번째 줄입니다.
line = f.readline()
line = line.strip()
print(line) # 3번째 줄입니다.
f.seek(0)
line = f.readline()
line = line.strip()
print(line) # 4번째 줄입니다.

f.close()
