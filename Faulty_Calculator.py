# #excercise
# #faulty calculator
# # design a caluc-e operator and the two numbers as input from the user and then return the result
#
# Scenario:
# Suppose that you are an invigilator in an exam. Calculator is not allowed for the exam. You discover somehow that
# students are planning to cheat in exam, using a calculator program in Python language. Somehow you get your hands
# on the calculator program and now you want to alter few results in calculator with your own provided results,
# so you can catch the students who are trying to cheat using the calculator program.
#
# The user will provide the following inputs:
#
# Operator
# The two numbers, between which the operator is applied
# All the results will be correct, except for these few:
#
# 45 * 3 = 555
# 56+9 = 77
# 56/6 = 4


print("Enter 1st number")
num1 = int(input())
print("Enter 2nd number")
num2 = int(input())
print("what you want?" '+' '+, - ,/, %,*')
num3 = input()

if num1==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1==56 and num2==6 and num3=='/':
    print("4")
elif num3=='*':
    num4=num1*num2
    print(num4)
elif num3=='+':
    plus=num1+num2
    print(plus)
elif num3=='-':
    diff=num2-num1
    print(diff)
elif num3=='/':
    div=num2/num1
    print(div)
elif num3=='%':
    mod=num2%num1
    print(mod)
else:
    print("Error! Please check your input")


