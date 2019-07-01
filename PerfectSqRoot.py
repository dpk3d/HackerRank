# Getting the Perfect Square
# Input Between 6000 to 7000 get the Perfect square root till last digit.
# 81 is perfect Sq root of 6561. 6561 == 81 == 9 == 3.
# Between 10 and 20 . perfecct is 16. 16 == 4  == 2 .


import math

def isperfect_sq(sr):
   return ((sr - math.floor(sr)) == 0)

def get_perfect_sq(num):
   c =0
   while(isperfect_sq(math.sqrt(num))):
      num = math.sqrt(num)
      c+=1
   return c

def calc1(c, num1, num2):
   flg  = True
   temp = num1
   arr = []
   while(temp <= num2):
      x = math.sqrt(temp)
      if (isperfect_sq(x)):
         arr.append([temp, x])
      temp+=1
   return arr

c =0
arr = calc1(c, 10,20)

for (i,e) in arr:
   print ('answer', e, get_perfect_sq(e)+1)
