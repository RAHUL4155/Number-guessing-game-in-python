def guessNumber(startRange, endRange):
    if startRange > endRange:
        return True


    mid = (startRange + endRange) // 2

   
    print(f"Is the number {mid}? (Y/N): ", end="")
    user = input().strip()

    
    if user in ("Y", "y"):
        print("Congratulation Geek! Successfully Guessed Number.")
        return False

    
    elif user in ("N", "n"):
        print(f"Is the actual number greater than {mid}? (Y/N): ", end="")
        user = input().strip()

        if user in ("Y", "y"):
            return guessNumber(mid + 1, endRange)
        elif user in ("N", "n"):
            return guessNumber(startRange, mid - 1)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            return guessNumber(startRange, endRange)
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        return guessNumber(startRange, endRange)


if __name__ == "__main__":
    print("Number Guessing Game in Python")
    
    
    startRange = int(input("Enter Start Range: "))
    endRange = int(input("Enter End Range: "))

    print(f"Think of a number between {startRange} and {endRange}. I will try to guess it!")

    out = guessNumber(startRange, endRange)

    if out:
        print("Couldn't guess it. Are you sure you answered correctly?")