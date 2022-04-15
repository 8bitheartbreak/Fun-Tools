#Fizz Buzz Customizable

def FizzBuzz(range_of_numbers, m1, m2):
    listInts = []

    for integers in range(1, (range_of_numbers + 1)):

        if integers % m1 == 0 and integers % m2 == 0:
            listInts.append("FizzBuzz")
        elif integers % m1 == 0:
            listInts.append("Fizz")
        elif integers % m2 == 0:
            listInts.append("Buzz")
        elif integers % m1 != 0 and integers % m2 != 0:
            listInts.append(integers)
    #parse text
    print(str(listInts).translate(str.maketrans({'[': '', ']': '', '\'': ''})))


fizzVal = 3  # ENTER A VALUE HERE
buzzVal = 5  # ENTER ANOTHER VALUE
iterations = 1000  # ENTER HOW MANY TIMES TO CHECK FIZZ BUZZ THROUGH

FizzBuzz(iterations, fizzVal, buzzVal)



