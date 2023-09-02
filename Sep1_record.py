#Exercise 1 - 짝수의 합

#Description
#정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을
#return 하도록 solution 함수를 작성해주세요.


#My solution
def solution(n):
    
    i = 1
    sum = 0
    
    for i in range(n+1):
        if i % 2 == 0:
            sum += i 
    return sum

#to loop numbers, write like for i in range(n+1), where argument is 'n' 


#Other solution

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

#range - starting from 2, increasing by 2, until given number n, so (n + 1)


#Exercise 2 - 배열 자르기

#Description
#정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
#numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

#My solution

def solution(numbers, num1, num2):
    return numbers[num1: num2 + 1]

#Remember
#list has its index starting from 0 
#Slicing a list, the last element is EXclusive, so must add 1 (num2 + 1)


#Exercise 3 - 외계행성의 나이

#Description
#우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
#입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
#a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다.
#나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

#My solution

def solution(age):
    result = ''
    answer = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    
    for i in str(age):
        result += (answer[i])
    return result
    
    #assigning each letters, into numbers - using dictionary
    #key: numbers, value: letters -- when answer[number], can get the letters
    #add to the string 'result' everytime, for every 'age' - should consider as a 'string' to split the digit as individuals



    
