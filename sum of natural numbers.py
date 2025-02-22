/* num = int(input("enter a number :"))
sum = (num*(num+1/2))
print("The sum of numbers is ",sum)


num1 = int(input("enter number1 :"))
num2 = int(input("enter number 2: "))
sum = num2*(num2+1/2)-(num1*(num1-1/2)+num1)
print(sum)*/


year= int(input("enatera year:"))
if((year%400==0)or (year%4==0 and year%100==0)):
 print(year,"is leap year")
else:
    print(year,"is not leap year")
