#Exercise 1 - 직각삼각형 출력하기

#Description
#"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다. 
#정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

#My solution: 

n = int(input())
m = 1
#for every n - print n rows // and n times for the last row (incrase 1 * for row)

for m in range(1, n+1):
    print(m * "*", end = '\n')

#Since we need to print * by increasing order, we use for, and range(1 + n+1), where n+1 is exclusive.
#Define another variable m, and use it as a repeating variable for 'for'
#Use '\n' to move to new row 

#Other solutions:

n = int(input())
for i in range(n):
    print('*'*(i+1))

#Can simplify range as range(n)


#Exercise 2 - 짝수 홀수 개수

#Description
#정수가 담긴 리스트 num_list가 주어질 때,
#num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

#My solution:

def solution(num_list):
    o = 0 #is the # of odd num
    e = 0 #even num
    answer = []
    
    for odd in num_list:
        if odd % 2 == 1:
            o += 1
    for even in num_list:
        if even % 2 == 0:
            e += 1
    answer.insert(0, e)
    answer.insert(1, o)
    return answer