import math

def fibonacci():
    iterations_done = 1

    first_num = int(input("Input the first number: "))
    second_num = int(input("Input the second number: "))
    iterations = int(input("Input the number of iterations(including the two starting numbers): "))

    print(first_num)
    print(second_num)

    numbers = [first_num, second_num]

    while iterations_done < iterations - 1:
        current_num = numbers[iterations_done] + numbers[iterations_done - 1]
        numbers.append(current_num)
        iterations_done += 1

    print(numbers)

    return numbers

def prime():
    number = int(input("Input the number to test if prime:"))
    square_root = math.sqrt(number)
    test_number = 2
    is_prime = True

    while test_number < square_root:
        if number % test_number == 0:
            is_prime = False
            print("The number " + str(number) + " is not prime.")
            return True
        test_number = test_number + 1
    print("The number " + str(number) + " is prime.")

def divider():
    first_num = int(input("What is the number you want to divide into?"))
    second_num = int(input("What is the number you want to divide by?"))

    third_num = first_num/second_num

    if first_num % second_num == 0:
        third_num = round(third_num)
        print(str(first_num) + " divided by " + str(second_num) + " is a whole number! It is " + str(third_num) + ".")
    else:
        print(str(first_num) + " divided by " + str(second_num) + " is not a whole number! It is " + str(third_num) + ".")


def main():
    option = ""
    math = ["Fibonaci", "Primes", "Divider"]
    abc = ["A","B","C"]
    for i,s in enumerate(math):
        print(abc[i] + ": " + s)
    option = input("Select an math tool:")
    
    if(option == abc[0] or option == math[0]):
        fibonacci()
    elif(option == abc[1] or option == math[1]):
        prime()
    elif(option == abc[2] or option == math[2]):
        divider()
    else:
        print("Invalid option.")
    
main()


