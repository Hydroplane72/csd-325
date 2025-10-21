# Matthew Rozendaal
# 09/30/2025
# Module 11.2 
# This program defines two functions to count the number of 1s from 1 to n, one using recursion and the other using a loop.
# I intentionally set the default currentNumber to 1 in the recursive function so we would not print 0.
# Even though it should not be necessary since we do the check in the main function, I added checks to ensure n is greater than 0 in both functions.

def recursive_count_ones( targetNumber: int,currentNumber:int = 1):
    """
    This function uses recursion to count the number of 1s from 1 to n.
    If n is 0, it returns 0 (base case).
    For other values, it adds 1 till we hit n.
    """
    if targetNumber <= 0:
        return
    else:
        print(f"Recursive call with targetNumber {targetNumber} currentnumber={currentNumber}")
        if currentNumber < targetNumber:
            recursive_count_ones(targetNumber, currentNumber + 1)
        
    return
        
def non_recursive_count_ones(n: int):
    """
    This function uses a loop to count the number of 1s from 1 to n.
    It iterates from 1 to n and counts each iteration.
    """
    if n <= 0:
        return
    count = 0
    for i in range(1, n + 1, 1):
        count += 1
        print(f"Non-recursive loop iteration {i}, count={count}")
    return

def main():
    while True:
        try:
            userInput = int(input("Enter a positive integer greater than 0: "))
            if userInput <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("\nInvoking Recursive Function:")
    recursive_count_ones(userInput)
    print("Finished Recursive Function.\n")

    print("Invoking Non-Recursive Function:")
    non_recursive_count_ones(userInput)
    print("Finished Non-Recursive Function.")

main()