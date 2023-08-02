Aug2_record.py

#Exercise 1 - 피자 나눠 먹기 (3)

#Description
#머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
#피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
#n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(slice, n): #input: # of slices // n people 

    pizza = n // slice #pizza - 2 pieces -> up to 10 pieces

    if (n % slice) != 0:
        pizza += 1
        
    return pizza 

#Other solutions:
#1
def solution(slice, n):
    return ((n - 1) // slice) + 1
#Very simplified and straight-forward, just write after return  

#2
def solution(slice, n):
    return n//slice + (1 if n%slice else 0)
#Uses if loop, after the quotient


#Exercise 2 - 배열의 평균값

#Description
#정수 배열 numbers가 매개변수로 주어집니다. 
#numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    sum = 0
    
    for index in range(1, len(numbers)+1):
        sum += numbers[index]
        avg = sum / len(numbers)
    return float(avg)

#정수 배열: array of letegers

def solution(numbers): #numbers: 정수 배열: array of letegers
    sum = 0
    for i in numbers:
        sum += i
        avg = sum / len(numbers)
    return avg

    if len(numbers) != 0:

        


#Exercise 3 - 옷가게 할인 받기

#Description
#머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
#구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.


def solution(price):
    
    if price >= 100000 and price < 300000:
        price = price * 0.95
        return int(price)
    elif price >= 300000 and price < 500000:
        price = price * 0.9
        return int(price)
    elif price >= 500000:
        price = price * 0.8
        return int(price)
    else:
        return int(price)


#Other solutions:

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

#Using dictionary is an intelligent idea,,



#Exercise 4 - 아이스 아메리카노

#Description
#머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 
#머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
#머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(money):
    answer = []

    answer.append(money // 5500) #cup of coffee
    answer.append(money % 5500) #left money
    return answer

#Other solutions:
#1
def solution(money):

    answer = [money // 5500, money % 5500]
    return answer

#2
def solution(money):
    return divmod(money, 5500)
#divmod() - making a tuple including the quotient(cup of coffee, in this case), and the remainder (the remaining money)



#Exercise 5 - 나이 출력

#Description
#머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
#나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

def solution(age):

    return (2022 - age) + 1 



#Exercise 6 - 배열 뒤집기

#Description
#정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
#num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    
    num_list.reverse()
    return num_list