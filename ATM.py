print("welcome to sbi")
n=int(input("enter the 4 digit pin number:"))
m=20000
if n==1319:
    print("1-withdraw")
    print("2-balence enquiry")
    print("3-fast cash")
    c=int(input("enter your choice"))
    if c==1:
        w=int(input("enter your amount"))
        if w<m and w%100==0:
            print("pleace collect your money")
        else:
            print("invalid cash")
    elif c==2:
            print("your balence",m)
    elif c==3:
            print("1-50000")
            print("2-10000")
            print("3-15000")
            print("4-20000")
            f=int(input("enter your fast cash option;"))
            if f==1 and 5000<m:
                print("place take cash of 5000")
            elif f==2 and 10000<m:
                print("place take cash of 10000")
            elif f==3 and 15000<m:
                print("place take cash of 15000")
            elif f==4 and 20000<m:
                print("place take cash of 20000")
            else:
                print("invalid cash choice")
    else:
        print("invalid choice")
else:
    print("invalid pin")