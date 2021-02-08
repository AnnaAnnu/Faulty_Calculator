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


