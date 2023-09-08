#Problem 3, continuing from last day = Problem 1 - 모스부호 (1)

#Description
#머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다.
#그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다.
#문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
#모스부호는 다음과 같습니다.

"""
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
"""
#제한사항
#1 ≤ letter의 길이 ≤ 1,000
#return값은 소문자입니다.
#letter의 모스부호는 공백으로 나누어져 있습니다.
#letter에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#해독할 수 없는 편지는 주어지지 않습니다.
#편지의 시작과 끝에는 공백이 없습니다.

#My solution

def solution(letter):
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    answer = ''

    let = letter.split(' ') #split the 'morses'(.--_.-.. these) with SPACES, into a LIST different seperate elements
    for sign2 in let: #for each element, splited AFTER spaces
        answer += morse[sign2]
    return answer


#Other approach

def solution(letter):
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    return ''.join([morse[i] for i in letter.split(' ')])

#can write into one single line (explained from the right to left)
    #1. split letter by spaces ' '
    #2. use loop, to get each letter into alphabet - alphabet = morse[i]
    #3. join the alphabet into a string '' - ''.join(), and include [], as it is a LIST
    #4. return the string 



#Problem 2 - 가위 바위 보

#Description
#가위는 2 바위는 0 보는 5로 표현합니다.
#가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, 
#rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

#제한사항
#0 < rsp의 길이 ≤ 100
#rsp와 길이가 같은 문자열을 return 합니다.
#rsp는 숫자 0, 2, 5로 이루어져 있습니다.


#My solution:

def solution(rsp):
    answer = ''

    for num in rsp:
        if num == '2':
            answer += '0'
        elif num == '0':
            answer += '5'
        elif num == '5':
            answer += '2'
    return answer


#Another approach: - use dicitonary, and make consisely 

dic = {'2':'0', '0':'5', '5':'2'}
return ''.join(dic[i]) for i in rsp) - we use JOIN function to attach to a STRING



#Problem 3 - 구슬을 나누는 경우의 수

#Description
#머쓱이는 구슬을 친구들에게 나누어주려고 합니다.
#구슬은 모두 다르게 생겼습니다.
#머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때,
#balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.


#제한사항
#1 ≤ balls ≤ 30
#1 ≤ share ≤ 30
#구슬을 고르는 순서는 고려하지 않습니다.
#share ≤ balls

from math import factorial as fac

def solution(balls, share):
    
    return fac(balls)/(fac(share)*fac(balls-share))

#can write using combination - requiring the use of FACTORIAL
    #To use FACTORIAL - fac(), must import from math library 'math' ==> from math import factorial
    #Here, to use, I renamed it as 'fac'


#Another approach

#Combination can be done just through the math library - math.comb(n, k)

import math

def solution(balls, share):
    return math.comb(balls, share)