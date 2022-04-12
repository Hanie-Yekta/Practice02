import math

print("Choose your operation:\n1.sum \n2.sub \n3.mul",
      "\n4.div \n5.pow \n6.sin \n7.cos \n8.tan \n9.cot")
opr=int(input())

#mohasebat sum
if opr==1:
    print("\nEnter your first value:")
    val1=float(input())
    print("\nEnter your second value:")
    val2=float(input())
    sum=val1+val2
    print("\nSum:",sum)

#mohasebat sub
elif opr==2:
    print("\nEnter your first value:")
    val1=float(input())
    print("\nEnter your second value:")
    val2=float(input())
    sub=val1-val2
    print("\nSub:",sub)

#mohasebat mul
elif opr==3:
    print("\nEnter your first value:")
    val1=float(input())
    print("\nEnter your second value:")
    val2=float(input())
    mul=val1*val2
    print("\nMul:",mul)

#mohasebat div
elif opr==4:
    print("\nEnter your first value:")
    val1=float(input())
    print("\nEnter your second value:")
    val2=float(input())
    div=val1/val2
    print("\nDiv:",div)

#mohasebat pow
elif opr==5:
    print("\nEnter your value:")
    val1=float(input())
    print("\nEnter the value of pow:")
    val2=int(input())
    power=math.pow(val1,val2)
    print("\Pow:",power)

#mohasebat sin
elif opr==6:
    print("\nEnter the value(Rad):")
    val1=int(input())
    print("\nSin:",math.sin(val1))

#mohasebat cos
elif opr==7:
    print("\nEnter the value(Rad):")
    val1=int(input())
    print("\nCos:",math.cos(val1))

#mohasebat tan
elif opr==8:
    print("\nEnter the value(Rad):")
    val1=int(input())
    print("\nTan:",math.tan(val1))

#mohasebat cot
elif opr==9:
    print("\nEnter the value(Rad):")
    val1=int(input())
    cot=(1/(math.tan(val1))
    print("\nCot:",cot)
    
