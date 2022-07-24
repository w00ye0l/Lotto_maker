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

        print('꼭 넣고 싶은 숫자들이 있나요?? Y or N')
        want_numbers_question = input()

        if want_numbers_question == "Y":
            print("꼭 넣고 싶은 숫자들이 몇개입니까??")
            want_numbers_count = int(input())

            want_numbers_list = []
            for i in range(1,want_numbers_count + 1):
                print("원하시는 {0}번째 숫자을 입력해주세요".format(i))
                want_numbers_list.append(int(input()))
            numbers = []
            for i in range(n):
                number = random.sample(range(1, 46), 6 - want_numbers_count)
                number += want_numbers_list

                number = set(number)
                while True:
                    number = set(number)
                    if len(number) == 6:
                        break
                    if len(number) != 6:
                        k = random.sample(range(1, 46), 6 - len(number))
                        number.update(set(k))
                number = list(number)
                number.sort()
                numbers.append(number)
                self.numbers = numbers
        else:
            numbers = []
            for i in range(n):
                number = random.sample(range(1, 46), 6)
                number.sort()
                numbers.append(number)
                self.numbers = numbers
        # print(numbers)

    def compute_number(self):
        for i in range(self.n):
            l_dic = {}
            result = []
            for j in self.numbers[i]:
                if not j in l_dic:
                    l_dic[j] = 1
                else:
                    l_dic[j] += 1
            l_dic = sorted(l_dic.items(), key=lambda x: x[1], reverse=True)
            temp = l_dic[:6]
            for i in range(6):
                result.append(temp[i][0])

        print(f'나만의 숫자 횟수: {self.n}, 구매할 로또 번호: {result}', end='\n\n')

    def buy(self):
        for i in range(self.t):
            self.make_number()
            self.compute_number()

lotto = Lotto()
lotto.compute_money()
lotto.buy()