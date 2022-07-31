import random
import requests
import json
from pprint import pprint

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
        if self.want_numbers_question == "Y":
            print("몇개의 숫자를 원하십니까??")
            want_numbers_count = int(input())
            self.want_numbers_count = want_numbers_count

            want_numbers_list = []
            for i in range(want_numbers_count):
                print("원하시는 {0}번째 숫자을 입력해주세요".format(i + 1))
                want_numbers_list.append(int(input()))

            n = int(input('나만의 숫자:'))
            self.n = n
            numbers = []

            for i in range(n):
                number = random.sample(range(1, 46),6 - want_numbers_count)
                number += want_numbers_list
                while True:
                    number = set(number)
                    if len(number) == 6:
                        break
                    else:
                        k = set(random.sample(range(1, 46),6 - len(number)))
                        number.update(k)
                number = sorted(list(number))
                numbers.append(number)
                self.numbers = numbers
        else:
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
        result = []
        self.cumulative_sum = {}
        for i in range(self.n):
            for j in self.numbers[i]:
                self.cumulative_sum[j] = self.cumulative_sum.get(j, 0) + 1
        self.cumulative_sum = sorted(self.cumulative_sum.items(), key=lambda  x:(-x[1]))
        temp = self.cumulative_sum[:6]
        for i in range(6):
            result.append(temp[i][0])
        print(f'나만의 숫자로 랜덤 돌린 횟수: {self.n}, 구매할 로또 번호: {result}', end='\n\n')

    def want_number(self):
        want_numbers_question = input("본인이 원하는 숫자들이 있습니까? Y or N \n")
        self.want_numbers_question = want_numbers_question

    def cumlative_Sum(self):
        cumlative_sum = {}
        self.cumlative_sum = cumlative_sum

    def buy(self):
        for i in range(self.t):
            self.want_number()
            self.make_number()
            self.compute_number()
    def win_Lottery(self):
        want_number_winlotto = input("N회차 당첨번호를 알고 싶으신게 있습니까? Y or N \n")
        self.want_number_winlotto = want_number_winlotto
        if want_number_winlotto == "Y":
            print("N회차 이십니까? 1 ~ 1025")
            winlotto_number = int(input())
            
            url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'
            url = url.format(winlotto_number)
            response = requests.get(url).json()

            drw_dt = response.get('drwNoDate', None)
            no_1 = response.get('drwtNo1', None)
            no_2 = response.get('drwtNo2', None)
            no_3 = response.get('drwtNo3', None)
            no_4 = response.get('drwtNo4', None)
            no_5 = response.get('drwtNo5', None)
            no_6 = response.get('drwtNo6', None)
            bonus_no = response.get('bnusNo', None)

            print('Draw lottery date :', drw_dt)
            print('Number 1 :', no_1)
            print('Number 2 :', no_2)
            print('Number 3 :', no_3)
            print('Number 4 :', no_4)
            print('Number 5 :', no_5)
            print('Number 6 :', no_6)
            print('Bonus Number :', bonus_no)
lotto = Lotto()
lotto.win_Lottery()
lotto.compute_money()
lotto.buy()