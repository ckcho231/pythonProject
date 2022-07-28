import random                          # 난수를 만드는 random 모듈을 사용합니다.
correct_answer = random.randint(1, 20)  # 1에서 20사이의 난수를 만듭니다.

count = 0                               # 숫자형 변수 count를 만들고 0으로 초기화 합니다.

while True:                            # while 반복문 조건이 무조건 True이므로 무한으로 반복
    number = int(input("숫자를 입력하세요: "))
    count += 1
    if correct_answer == number :       # 난수와 일치하면 while문을 빠져 나옵니다
        break
    elif correct_answer > number :
        print(number, "보다 큽니다!")
    else :
        print(number, "보다 작습니다!")

# while 반복문을 빠져 나왔으니 결과를 출력 합니다.
print("정답입니다!")
print(count, "번 만에 정답을 맞추셨군요~~~")


print("이것은 PC에서 작성하였습니다.");