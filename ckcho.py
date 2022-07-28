def addNum(a, b):
    return f"{a} + {b} = {a + b}"

#
# 여기에 함수 설명을 작성한다
# 함수 이름 : 피보머시기
# 작성자
# 최초 작성 일시 :


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def exam(num1, num2=2):
    print('a=', num1, 'b=', num2)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

class fourCal:
    def __init__(self):
        self.fir = None
        self.sec = None

    def setdata(self, fir, sec):
        self.fir = fir
        self.sec = sec

    def add(self):
        result = self.fir + self.sec
        return result

