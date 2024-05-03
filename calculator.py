# IMPORTING LIABRARIES
import math
from tqdm import tqdm
import time
  
#This function is designed for the INTRODUCTION TO OUR CALCULATOR PROGRAM

def Welcome():
    print("\n\n----------------------------------------------------------",end=" ")
    print("\n|                                                        |",end = " ")
    print("\n|              SCIENTIFIC CALCULATOR.....                |", end="\n")
    for i in tqdm (range (100), desc="|Loading..."):
        time.sleep(0.02)
        pass
    print("----------------------------------------------------------")

# This function is designed for performing the ADDITION OF n numbers

def Addition():
    print("how many numbers you want to add?")
    num_sum=int(input())
    sum=0
    for x in range(num_sum):
        num_add = list(map(int,input("Enter Number "+ " " + str(x+1) + " ").split()))
        for y in num_add:
            sum+=y
    print("\n \n THE SUM OF ALL NUMBERS IS : ", sum, end="\n")  

# This function is designed for performing the SUBTRACTION of n numbers

def Subtraction():
    print("\n For How many variables You want to do subtraction?",end="\n")
    num_diff = int(input("\n Enter the Total number of Operands"))
    if num_diff == 1:
        print("\n Invalid Operation or please Give atleast two operands to perform Subtraction", end="\n")
    elif num_diff==2:
        Num1=int(input("Enter First Number  "))
        Num2=int(input("Enter Second Number  "))
        diff=Num1-Num2
        print("\n\n THE DIFFERENCE BETWEEN TWO NUMBERS ", Num1 , "and", Num2 ,"is :",diff, end="\n")
    elif num_diff==3:
        Num1=int(input("Enter First Number  "))
        Num2=int(input("Enter Second Number  "))
        Num3=int(input("Enter Third Number  "))
        diff=Num1-Num2-Num3
        print("\n\n THE DIFFERENCE BETWEEN THREE NUMBERS  ", Num1 , "and", Num2 , "and", Num3, "is :",diff, end="\n")
    elif num_diff>=4:
        numbers=[]
        for x  in range(num_diff):
            for i in (input("Enter Number " + str(x+1)+ " ").split()):
                numbers.append(i)
            diff=int(numbers[0])
            for number in numbers[1:]:
                diff = diff - int(number)
        print(" \n \n THE DIFFERENCE BETWEEN ALL THE NUMBERS ", diff, end="\n\n")

# This function is designed to perform MULTIPLICATION of two or more numbers

def Multiplication():
    print("\n How many numbers do you want to multiply?", end="\n")
    choice=int(input("\n Enter the Total number of Multiplicands :"))
    if choice==1:
        print("\n Multiplication of one number is not possible ", end="\n")
        print("\n Do You wish to multiply that number with itself :", end="\n")
        option=str(input("Yes or No,enter (Y,N) "))
        if option=='y' or option=="Y":
            Number=float(input(" \n Enter the number which you want to multiply with itself ", end="\n"))
            result=Number**2
            print("\n \n THE MULTIPLICATION OF THAT NUMBER ", Number , "WITH ITSELF IS : ", result, end="\n\n")
    elif choice==2:
        Number1=float(input("\n Enter first number "))
        Number2=float(input("\n Enter second number "))
        result=Number1*Number2
        print("\n \n THE MULTIPLICATION OF NUMBERS ", Number1, "AND ", Number2, "IS : ", result, end="\n\n")
    elif choice>=3:
        numbers=[]
        for x  in range(choice):
            for i in (input("Enter Numbers "+ str(x+1)+ " ").split()):
                numbers.append(i)
            result=1
            for x in numbers:
                result=result*float(x)
        print("\n \n THE MULTIPLICATION OF THE NUMBERS IS : ",result, end="\n\n")

#This function is designed to perform DIVISION of two numbers

def Division():
    print("\n 1. Do the division for the integers ",end="\n")
    print("\n 2. Do the division for the floating point numbers ",end="\n")
    choice=int(input("\n Enter 1 or 2 "))
    if choice==1:
        Num1=int(input("\n Enter the first number (Dividend): "))
        Num2=int(input("\n Enter the Second NUmber (Divisor) "))
        if Num2==0:
            print("\n ERROR!!!",END="\n")
            print("\n\n The Division of a Number by 0 is not possible",end="\n")
        else:
            Division=Num1/Num2
            print("\n\n THE QUOTIENT CALCULATED BY DIVIDING NUMBERS ",Num1 , " and", Num2, "is : ", Division, end="\n\n")
    elif choice==2:
        Num1=float(input("Enter the first number (Dividend): "))
        Num2=float(input("Enter the Second NUmber (Divisor) "))
        if Num2==0:
            print("\n ERROR!!!",end="\n")
            print("\n\n The Division of a Number by 0 is not possible",end="\n\n")
        else:
            Division=Num1/Num2
            print("\n \n THE QUOTIENT CALCULATED BY DIVIDING NUMBERS ",Num1 , " and", Num2, "is : ", Division, end="\n\n")
    else:
        print("\n ERROR!!!! ..... \n",end="\n")
        print("INVALID CHOICE PLEASE CHOOSE BETWEEN 1 OR 2", end="\n\n")

# This funciton is designed for CALCULATING THE MODULUS OF the numbers

def Modulus():
    x=float(input("\n Enter  First number : "))
    y=float(input("\n Enter divisor : "))
    modulus=x%y
    print("\n\n THE MODULUS BETWEEN TWO NUMBERS ",x ,"and", y , "is :{:.2f}".format(modulus))

# This function is designed for CALCULATING THE POWERS taking BASE AND  EXPONENTIAL  values from the user

def Powers_Exponents():
    Base=float(input("\n Enter the Base NUmber whose powers you have to calculate : "))
    exponent=float(input("\n Enter the exponent Number which will be given as power to base  : "))
    power=Base**exponent
    print("\n\n THE VALUE OF THE NUMBER ", Base, "TO THE POWER OF ",exponent,"is : ", power ,end="\n\n")

# This function is designed to CALCULATE THE ROOTS OF A NUMBER OR 1/NTH POWER OF A NUMBER

def Calculating_Roots():
    Number=float(input("\n Enter the number whose root you want to find : "))
    exponent=float(input("\n Which Root You want ? "))
    result=pow(Number,1/exponent)
    if exponent==2:
        print("\n THE SQUARE ROOT OF ", Number, "is : ", result, end="\n")
    elif exponent==3:
        print("\n THE CUBE ROOT OF ", Number, "is : ", result, end="\n")
    else:
        print("\n THE NTH ROOT OF ", Number, "is : ", result, end="\n")

# This function is designed to calculate the FACTORIAL OF A NUMBER

def Factorial():
    factorial=1
    Number=float(input("\n Enter a Number whose factorial You want to be Calculated : "))
    if (Number>=1) and Number.is_integer()==True:
        for fact in range(1, int(Number+1)):
            factorial=factorial*fact
        print("\n\n THE FACTORIAL OF THE GIVEN NUMBER  ", Number,"is : ", factorial, end="\n\n")
    else:
        print("\n")
        for i in tqdm (range (100), desc=" ERROR !!!!..."):
            time.sleep(0.01)
            pass
        print("\n The FACTORIAL cannot be calculated for NEGATIVE NUMBERS and DECIMAL NUMBERS !!!!!!!!!", end="\n\n")

# This function is designed to calculate the TRIGNOMETRY

def Trignometry():
    print("\n WHICH TRIGNOMETRIC FUNCTION DO YOU WANT TO USE \n\n 1. SIN \n 2. COS \n 3. TAN \n 4. SEC \n 5. COSEC \n 6. COT ", end="\n")
    choice=float(input("\n Enter Choice (1-6)"))
    x=float(input("\n Enter the values in degrees "))
    x=(x/180)*3.14159265359
    if (choice==1):
        print(math.sin(x), end="\n")
    elif(choice==2):
        print(math.cos(x), end="\n")
    elif(choice==3):
        print(math.tan(x), end="\n")
    elif(choice==4):
        print(1/math.cos(x), end="\n")
    elif(choice==5):
        print(1/math.sin(x), end="\n")
    elif(choice==6):
        print(1/math.tan(x), end="\n")
    else:
        print("\n\n INVALID CHOICE !!!! \n \n Please Enter a VALID CHOICE(1-6)",end="\n ")
    return(0)

# This function  is designed for calculating the LOGARITHMIC VALUES

def logarithm():
    print("\n Which type of logarithms do you want to calculate ?", end="\n")
    print("\n 1.  NATURAL LOGS , (Base=e or ln)", end="\n")
    print("\n 2. LOGS WITH A BASE AND VALUE", end="\n")
    choice=int(input("\n Enter 1 or 2 "))
    if choice==1:
        Base=float(input("\n Enter a Base Number whose log you want to calculate "))
        print("\n\n THE NATURAL LOG OF THE NUMBER ", Base ," is : ", math.log(Base))
    elif choice==2:
        Base=float(input("\n Enter a Base Number whose log you want to calculate "))
        Exponent=float(input("\n Enter a exponent number which will the log base "))
        print("\n \n THE LOG OF ", Base ," WITH LOG BASE ", Exponent ,"is : ", math.log(Base, Exponent), end="\n\n")
    else:
        print("\n Print INVALID CHOICE!!!! \n\n")
        print("Enter a choice between 1 or 2 ")

# This function  is designed for calculating the EUCLEDIAN DISTANCE BETWEEN TWO POINTS

def Eucledian_distance():
    x1=float(input("\n Enter the x coordinate of the first point (x1) "))
    x2=float(input("\n Enter the x coordinate of the second point (x2) "))
    y1=float(input("\n Enter the y coordinate of the first point (y1) "))
    y2=float(input("\n Enter the y coordinate of the second point (y2) "))
    Eucledian_distance=((x2-x1)**2 + (y2-y1)**2)**0.5
    print("\n \n THE EUCLEDIAN DISTANCE BETWEEN TWO POINTS ","(",x1,",",y1,")","and","(",x2,",",y2,")","is : ", Eucledian_distance, end="\n\n")

# This function is designed to CALCULATE AREA OF DIFFERENT POLYGONS 

def Area():
    print("\n Which Figure Area do you want to calculate ? \n\n 1. RECTANGLE \n 2. SQUARE \n 3. TRIANGLE \n 4. CIRCLE \n 5. REGULAR POLYGON  ", end="\n")
    choice=int(input("\n Enter a Choice (1-5)"))
    if choice ==1:
        length=float(input("\n Enter The Length of Rectangle : "))
        breadth=float(input("\n Enter The Breadth of Rectangle : "))
        print("\n\n THE AREA OF RECTANGLE IS : ", length*breadth, end="\n")
    elif choice==2:
        side=float(input("\n Enter The Side of Square : "))
        print("\n\n THE AREA OF SQUARE IS : ", side*side, end="\n")
    elif choice==3:
        height=float(input("\n Enter The height of Triangle : "))
        breadth=float(input("\n Enter The Breadth of Triangle : "))
        print("\n\n THE AREA OF TRIANGLE IS : ", 0.5*breadth*height, end="\n")
    elif choice==4:
        Radius=float(input("\n Enter The Radius of Circle : "))
        print("\n\n THE AREA OF CIRCLE IS : {:.4f}".format( math.pi*Radius*Radius), end="\n")
    elif choice==5:
        no_of_sides=int(input("\n Enter no. of sides  of the REGULAR POLYGON : "))
        length=float(input("\n Enter Length of side :"))
        ans=length*length*no_of_sides/4*math.tan(3.14159265359/no_of_sides)
        print("{:.4f}".format(ans))
    else:
        print("\n \n  INVALID CHOICE !!! PLEASE ENTER A VALID CHOICE(1-5) ",end="\n")

#  THE MAIN MENU 

def Calculator():

    Welcome()
    print("\n WHAT DO YOU WANT TO DO?", end="\n")
    print("\n MAIN MENU : ", end="\n\n")
    print("\n 1. ADDITION ", end="\n")
    print("\n 2. SUBTRACTION ", end="\n")
    print("\n 3. MULTIPLICATION ", end="\n")
    print("\n 4. DIVISION  ", end="\n")
    print("\n 5. TAKING MODULUS(REMAINDER) OF NUMBERS ", end="\n")
    print("\n 6. CALCULATE THE POWERS OR EXPONENTS  ", end="\n")
    print("\n 7. CALCULATE THE ROOTS OR 1/nth POWERS OF A NUMBER ", end="\n")
    print("\n 8. CALCULATE THE FACTORIAL ", end="\n")
    print("\n 9. TRIGNOMETRY ", end="\n")
    print("\n 10. CALCULATE THE LOGARITHMICS AND NATURAL LOGS ", end="\n")
    print("\n 11. CALCULATE THE EUCLEDIAN DISTANCE BETWEEN TWO POINTS  ", end="\n")
    print("\n 12. CALCULATE THE AREA OF VARIOUS SHAPES AND POLYGONS ", end="\n")
    print("\n\n PLEASE ENTER A VALID CHOICE (1-12) ", end="\n\n")
    choice=int(input("ENTER YOUR CHOICE(1-12)?"))

    if choice==1:
        Addition()
    elif choice==2:
        Subtraction()
    elif choice==3:
        Multiplication()
    elif choice==4:
        Division()
    elif choice==5:
        Modulus()
    elif choice==6:
        Powers_Exponents()
    elif choice==7:
        Calculating_Roots()
    elif choice==8:
        Factorial()
    elif choice==9:
        Trignometry()
    elif choice==10:
        logarithm()
    elif choice==11:
        Eucledian_distance()
    elif choice==12:
        Area()
    else:
        print("\n\n INVALID CHOICE !!!!!! ", end="\n")
        print("\n \n PLEASE ENTER A VALID CHOICE (1-12) ", end="\n\n")

# THE MAIN FUNCITON

if __name__=="__main__":

    print("\n\n SCIENTIFIC CALCULATOR PROGRAM", end="\n")
    print("\n")
    for i in tqdm (range (100), desc=" INITIALIZING..."):
        time.sleep(0.01)
        pass
    Calculator()

    while True:
        deci=input("\n DO YOU WANT TO CONTINUE? (Yes or No) ?")
        if deci=="Y" or deci=='y' or deci=='Yes' or  deci=='yes':
            Calculator()
        else:
            break
