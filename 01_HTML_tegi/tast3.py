#=======================================
# random_example.py
# Module example using the random module
#=======================================
import random
# print 14 random integers
for cntr in range(1,15):
    print (random.randint(1,10))

#silly example 2...still silly, but better
def DoTwo(num1,num2):
    print (('%d + %d = %d') % (num1,num2,num1+num2))
    print (('%d * %d = %d') % (num1,num2,num1*num2))
    print (('%d - %d = %d') % (num1,num2,num1-num2))
    print ('\n')
DoTwo(1,2)
DoTwo(1,4)
DoTwo(10,5)
