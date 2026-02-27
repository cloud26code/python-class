# conditional statement
# condition
#conditional operators
# > greater than
# < less than
# == is equal
# != not equal
# >= greater than or equal
# <= less than or equal

print(25>20)
print(15<20)
print(6==6)
print(3!=4)
print(66>=76)
print(34<=32)


value = 35
val = 25
print(value>=val)

# if single
#if-slse two block
#if-elif-else multiblock

if 60 > 40:
    print("60 is greater than 40")

if 50 < 40:
    print("50 less than 40")

# write a program to show marks and find its percentage
#say congratulation if marks are above 70.
marks = int(input("enter your marks:"))
if marks> 60:
    print("congratulation you're passed",marks)
    percentage = marks/100*100
    print("your percentage is:",percentage,"%")


marks = int(input("enter your marks:"))
if marks > 70:
    print("congratulation you're passed",marks)
    percentage = marks/100*100
    print("your percentage is:",percentage,"%")
    