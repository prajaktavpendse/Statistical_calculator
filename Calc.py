import statistics
#from scipy import stats


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def square(a):
    return a * a


def squareroot(a):
    return a ** 0.5

def mode(l):
    return statistics.mode(l)

def variance(l):
    return statistics.variance(l)

def standardized_score(l):
    x=[]
    for i in  len(l):
        x[i]=(l[i]-mean(l))/standardized_score(l)
    return x


def proportion(l):
    return 0

def mean(l):
    return statistics.mean(l)






class Calc:
    def my_function(self):
        return 0

    if __name__ == "__main__":
        a = float(input("Enter first number:"))
        b = float(input("Enter second number:"))
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Square")
        print("6.Sqroot")
        # print("7.Mode")
        # print("8.Variance of population proportion")
        # print("9.Standardized score")
        # print("10.Proportion")
        # print("11.Sample Mean")
        print("7.Statistical calculator")
        choice = int(input("Enter your choice:1/2/3/4/5/6/7  :"))


    if choice == 1:
     print(addition(a, b))

     #result = addition(a, b)
        #return result

    elif choice == 2:
     print(subtraction(a, b))
     #result = subtraction(a, b)
      #  return result

    elif choice == 3:
     print(multiply(a, b))
     #result = multiply(a, b)
      #  return result

    elif choice == 4:
     print(division(a, b))
     #result = division(a, b)
      #  return result

    elif choice ==5:
     print(square(a))
      #  result = square(a)
       # return result

    elif choice == 6:
     print(squareroot(a))
      #  result = squareroot(a)
       # return result

    elif choice ==7:
        list=[]
        n=int(input("enter number of elements:"))
        for i in range(0,n):
            print("Enter a number : ")
            element=int(input())
            list.append(element)


        print("The choices are : ")
        print("1.Mode")
        print("2.Variance of population proportion")
        print("3.Standardized score")
        print("4.Proportion")
        print("5.Sample Mean")

        choice1=int(input(print("Enter choice 1/2/3/4/5 :")))

        if choice1 ==1:
            print("Mean is : %s " % mean(list))

        elif choice1==2:
            print("Variance is : %s" % variance(list))

        elif choice1==3:
            print("Standardized score is : %s" %standardized_score(list))

        elif choice1==4:
            print("Proportion is : %s"%proportion(list))

        elif choice1==5:
            print("Mean is : %s"%mean(list))

        else:
            print("wrong choice")





    else:
      print("invalid choice")