
#enumerate() 
#returns tuple, containing list's element and its position - (position, element)

#example
letters = ['A', 'B', 'C']
for i in enumerate(['A', 'B', 'C']):
    print (i)
#returns:
#(0, 'A')
#(1, 'B')
#(2, 'C')

#for n, letter in enumerate(['A', 'B', 'C']):


#Practices

#짝수는 싫어요
#Description

#정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = [i for i in range(1, n+1) if (i-2)%2 != 0]
    return answer

#use one-line for loop 
#need to define range - from 1, to n (n+1 as it is exclusive)
#condition - for NOT even numbers





#피자 나눠 먹기 1

#Description
#머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
#피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

def solution(n):
    
    ans = n // 7
    
    if n % 7 != 0:
        ans += 1
        return ans
    else:
        return ans


#Another approach
import math

def solution(n):
    return math.ceil(n/7)

#.ceil() returns the rounded UP value 
#to use this, need to recall math - import math




#피자 나눠 먹기 (2)

#Description
#머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
#n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(n):
pizza = 1 #initial value 
    
    while (pizza * 6) % n != 0: #infinite loop - when total pieces is NOT 6 mult
        pizza += 1 #add 1 more pizza - until it becomes mult of 6 (0 remainder)
    
    return pizza 

#another approach

def solution(n):

    pizza = 6
    while (pizza * 6) % n != 0:
        pizza += 6 #continuously add 6, until remainder is 0
    return pizza
