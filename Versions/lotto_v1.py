import random


class Lotto():
    def __init__(self):
        print('로또 번호 생성기!')

    def compute_money(self):
        money = int(input('보유금액(단위: 원): '))
        self.money = money
        t = money // 1000
        self.t = t
        self.c_money = t * 1000
        self.r_money = money % 1000
        print(f'사용금액: {self.c_money}원, 거스름 돈: {self.r_money}원', end='\n\n')

    def make_number(self):
        n = int(input('나만의 숫자: '))
        self.n = n
        numbers = []
        for i in range(n):
            number = random.sample(range(1, 46), 6)
            number.sort()
            numbers.append(number)
            self.numbers = numbers
        # print(numbers)

    def compute_number(self):
        l_dic = {}
        result = []

        for i in range(self.n):
            temp = []
            for j in self.numbers[i]:
                if not j in l_dic:
                    l_dic[j] = 1
                else:
                    l_dic[j] += 1
            print(l_dic)

        l_dic = sorted(l_dic.items(), key=lambda x: x[1], reverse=True)
        print(l_dic)
        temp = l_dic[:6]
        print(temp)

        for i in range(6):
            result.append(temp[i][0])
        result.sort()

        print(f'나만의 숫자로 랜덤 돌린 횟수: {self.n}, 구매할 로또 번호: {result}', end='\n\n')

    def buy(self):
        for i in range(self.t):
            self.make_number()
            self.compute_number()


lotto = Lotto()
lotto.compute_money()
lotto.buy()
