#operators in python

num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

# Arithmatic operation
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)  
print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder i.e. discarding the numbers after decimal point
print(num2 % num1)   # this is called modulus i.e. the reminder after division
print(3 ** 2) 

# Python supports BODMAS rule when multiple operators are in line

print(5 * 4 + 1)          # first multilpication will be executed
print(1 + 5 * 4)          # same as above first multilpication will be executed
print(5 * (4 + 1) )       # first brackets then rest 

# Comparison Operator
# == checks whether left hand side and right hand side is equal

print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS
# Let's explore < > <= >=

print(3 != 2)
 
print(3 > 2)
print(3 < 2)
 
print(3 >= 3)
print(3 >= 2)
 
print(3 <= 2)

#Assignment Operator
# += is a shortcut for add and assign 

num = 4
print(num)

num += 1   # is equivalent to num = num + 1
print(num) 
# -= is a shortcut for subtract and assign

num = 4
print(num)

num -= 1   # is equivalent to num = num - 1
print(num) 
num = 4
num *= 2
print(num)

num = 4
num /= 2
print(num)

#Logical Operators
# Three cases of AND

print(True and True)
print(True and False)   # same as False and True
print(False & False)    # instead of and, you can use &

# Three cases of OR
 
print(True or True)   
print(True or False)
print(False | False)  

# not is opposite of something (bool)

print(not True)
print(not False)
