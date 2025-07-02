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


    

def main():
    option = ""
    sequences = ["Fibonaci", "Primes", "Squares"]
    abc = ["A","B","C"]
    for i,s in enumerate(sequences):
        print(abc[i] + ": " + s)
    option = input("Select a sequence:")
    
    if(option == abc[0] or option == sequences[0]):
        fibonacci()
    
main()


