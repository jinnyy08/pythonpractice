#Problem 1 - 순서쌍의 개수

#Description
#순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
#자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.



#My solution

def solution(n):
    answer = []
    
    for i in range(1, n+1, 1):
        if n % i == 0:
            answer.append(i)
            answer.append(n/i) #this can be excluded, as we only need the LENGTH of the (a,b) ultimately
            if n == i:
                continue #this line can be reduced, by the single line method of return line
    return len(answer)/2



#Another approach (Optimal #1)
    #return the LENGTH of pair (num, n/num), which is within the form of list (a,b)
    
    return len([num for num in range(1, n+1) if n % num == 0]) 

    #Must put [ ], as we need the LENGTH of list (), containing num, n/num
        #this for loop, will create list () containing num, divisible by n (classified as 'factor')

    #num, will only the 'factor' of each n
        #But since we need LENGTH, LENGTH of a list containing 'factor' of n will return the SAME len 



#Another approach (Optimal #2)

def solution(n):
    answer = 0 #can be seen as the COUNT

    for i in range(1, n+1):
        if n % i == 0: 
            answer += 1
    return answer

    #Since we need the LENGTH of the pairs, 



#Another approach (Optimal #3)
def solution(n):
    answer = 0 #can be seen as the COUNT

    for i in range(n+1): #i can start from 0 - so need to state as range(n+1)
        if n % i == 0: 
            answer += 1
    return answer
  
    #make a for loop - number starting from 1, up to n+1
        #If i is DIVISIBLE by n, you increase the COUNT by 1  



#Problem 2 - 개미 군단

#Description
#개미 군단이 사냥을 나가려고 합니다. 
#개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
#장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다.
# 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 
#사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.

#My solution

def solution(hp):
    answer = 0

    a = hp // 5 
    hp %= 5 #set up hp, as the REMAINDER after division of a

    b = hp // 3
    hp %= 3

    c = hp // 1

    return (a+b+c)

    for i in range(1, hp+1):
    if ((hp % 5) % 3) == 0:
        return j
        answer += j

    for i in range(1, hp+1):
    if (((hp % 5) % 3) % 1) == 0:
        return k
        answer += k

    return answer

    
    #장군개미 - multiple of 5 (strongest) -- a
    #병정개미 - multiple of 3 (2nd strongest) -- b
    #일개미 - multiple of 1 (3rd str) -- c

    #return the LARGEST a, quotient (hp // 5)
        #using that REMAINDER, find the LARGEST b, quotient (hp // 5) // 3
            #Using last REMAINDER, find the LARGEST c, quotient ((hp // 5) // 3) // 1

            #At the end, return the SUM of EACH count



#Another approach (Optimal #1)

def solution(hp):
    return ((hp // 5) + (hp % 5 // 3) + (((hp % 5) % 3) // 1))

    #don't get mixed up with // and %
    #// returns the QUOTIENT
    #% returns the REMAINDER after the division 




#Problem 3 - 모스부호 (1)

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