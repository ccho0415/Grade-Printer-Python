import sys
print ("Welcome to The Auto Gradebook")
while True:
        print ("Input Name")
        name = sys.stdin.readline().strip()
        if name == "Goodbye":
                print ("Bye Bye")
                sys.exit(0)     
        print ("Input Numerical Grade")
        x = sys.stdin.readline()
        try:
                x = int(x)
        except ValueError:
                print ("Stop Trying to Break Me!!!!")
                continue
        if x>=90 and x<=100:
                print (name,"got an A")
        elif x>=89 and x<=80:
                print (name,"got a B")
        elif x>=79 and x<=70:
                print (name,"got a C")
        elif x>=69 and x<=60:
                print (name, "got a D")
        elif x<=59 and x>=0:
                print (name,"You're Going To Need a Few Shots")
        else:
                print ("Stop It and Give me a Real Number")
