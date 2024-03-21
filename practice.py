name = input("Hello, WHat is your name? ")
print("Nice to meet you " + name + "we are going to do some math")

# what are some arithmetic operators?
## exponent operator is **
## multiplication is *
## division is /
## assigning operator is =
## addition is +
## remainder operation is %
## subtraction is -
## intergral division operator is //

num1 = int(input("Please, give a number"))
num2 = int(input("Please, give another number"))
#print(num1 + num2)
sum = num1 + num2 
multi = num1 * num2
divi = num1 / num2
subst = num1 - num2
remain = num1 % num2
inter = num1 // num2
expo = num1 ** num2
print("the sum of " + str(num1) + " and " + str(num2) + " is: " + str(sum) )
print("the product of " + str(num1) + " and " + str(num2) + " is: " + str(multi) ) 
print("the difference of " + str(num1) + " and " + str(num2) + " is: " + str(divi) ) 
print("the remainder of " + str(num1) + " and " + str(num2) + " is: " + str(subst) ) 
print("the remainder of " + str(num1) + " and " + str(num2) + " is: " + str(remain) ) 
print("the intergral difference of "+ str(num1) +" and "+str(num2)+" is: "+str(inter) )
print("the exponent product of "+str(num1)+" and "+str(num2) + " is: " + str(expo)) 
