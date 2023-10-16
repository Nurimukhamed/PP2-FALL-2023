#1 grams in ounces
def grams_in_ounces(grams):
    print(28.3495231 * grams)
grams=float(input())
grams_in_ounces(grams)

#2 F in C
a = float(input())
def func(a):
    print((5 / 9) * (a - 32))
func(a)

#3 rabbitsandchikens
def solve(numheads, numlegs):
    kur = (numlegs - numheads*2 )/2
    rab = numheads - kur
    return rab , kur

print(solve(35,94))
'''heads= int(input())
legs=int(input())
print(solve(heads,legs))'''

#4 prime numbers in list
def primenums(c):
    x=0
    for i in range(2,c):
        if(c%i==0):
            x=x+1
    if(x==0):
        print(c,end=' ')
list = input().split()
for i in range(0, len(list)):
    primenums(int(list[i]))
     
#5 permutations
from itertools import permutations
def perm(S):
    list = list(S)
perm=permutations(list)
for i in perm:
    print(i)

S=str(input())
perm(S)

    
#6 reverse
def reverse(list):
    for i in range(len(list)-1,-1,-1):
        print(list[i],end=' ')
    
list = [str(s) for s in input().split(' ')]
reverse(list)
    
#7 has_33
def has_33(list):
    for i in range(len(list)-1):
        if(list[i]==3 and list[i+1]==3):
            return True
    return False
list = [int(s) for s in input().split()]
print(has_33(list))

#8 spy game
def spy_game(list):
    for i in range(len(list)-2):
        if(list[i]==0 and list[i+1]==0 and list[i+2]==7):
            return True
    return False
list = [int(s) for s in input().split()]
print(spy_game(list))

#9 obyem sphery
import math
def obyem_sphery(r):
    return(float((4/3)* math.pi * r) )
r = int(input())
print(float(obyem_sphery(r)))

#10 unique num
def uniq(list):
    l=[]
    for i in list: 
        if i not in l: 
            l.append(i) 
    return(l)
    
list = [int(s) for s in input().split()] 

res_list = uniq(list)   
for i in res_list: 
    print(i, end=' ')

#11 is palindrome
def ispolindrome(s):
    if(s==s[::-1]):
        print("is polindrome")
    else:
        print("is not polindrome")
s=str(input())
ispolindrome(s)

#12 hisogram
def histogram(list):
    for i in range(len(list)):
        for j in range(list[i]):
            print('*',end='')
        print('\n')
list=[int(s) for s in input().split()]
histogram(list) 

#13 Guess the number
import random
def gsn(num):
    s=input("Hello! What is your name?")
    print("Well,",s,", I am thinking of a number between 1 and 20.")
    c = 1
    g = int(input("Take a guess:"))
    if(g<num):
            print("Your guess is too low.")
    else:
            print("Your guess is too hight.")
    while(g != num):
        g = int(input("Take a guess:"))
        
        if(g<num):
            print("Your guess is too low.")
        elif(g==num):
            c=c+1
            break
        else:
            print("Your guess is too hight.")
        c=c+1
    print("Good job, KBTU! You guessed my number in", c , "guesses!")
        
num = random.randint(1,20)
gsn(num)


    
