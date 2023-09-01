#Exercise 1 - 각도기

#Description
#각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다
#각 angle이 매개변수로 주어질 때 
#예각일 때 1, 직각일 때 2, 둔각일 때 3, 
#평각일 때 4를 return하도록 solution 함수를 완성해주세요.

#My Solution:

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4

#Other solution:

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4
        

#Exercise 2 - 양꼬치

#Description
#머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.
#정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 
#총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

#My Solution:

def solution(n, k):
    
    return n*12000 + (k - (n // 10)) *2000