import convert as cv

print("whcih unit you want to convert?\nChoose from c f kg ounce pound meter mile inch foot\n")


ch1 = input("From?")
ch2 = input("To?")

num = input("Please input the specific value\n")
if str.isdigit(num) == False:
    print("Please input numbers!!")
    exit
num = float(num)
#print(num, type(num))



cv.uc(ch1, ch2, num)