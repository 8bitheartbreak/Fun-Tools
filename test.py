# First to run
import time

#5th to run
def working():
    try:
        num1, op, num2 = input("Type in an equation. ").split()
        if num1 and num2.isdigit():
            print("OK, calculating...")
            time.sleep(0.6)

        else:
            print("You did not enter a number. ")
            time.sleep(0.6)
    except ValueError:
        print("Improper syntax. Enter like this: 5 + 7 ")
        time.sleep(0.2)
        run_calc()
    except ZeroDivisionError:
        print("0.0")
    return num1, op, num2

#3rd - function starts to run after call
def run_calc():
    #4th calls the working function above
    n1, op, n2 = working()
    #6th to run - the calculations take place here and repeats the action at the end
    if op == '+':
        ans = float(n1) + float(n2)
    elif op == '-':
        ans = float(n1) - float(n2)
    elif op == '*' or 'x':
        ans = float(n1) * float(n2)
    elif op == '/':
        ans = float(n1) / float(n2)
    else:
        print("You did not enter a proper operator! (+, -, * x, /)")
        time.sleep(0.5)
        run_calc()
    print("The answer is " + str(ans) + "!")
    run_calc()





#Second
run_calc()
