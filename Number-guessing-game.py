def guessNumber(start, end):
    if start > end:
        return True

    mid = (start + end) // 2
    user = input(f"Is the number {mid}? (Y/N): ").strip()

    if user == "Y" or user == "y":
        print("Congratulations! I guessed your number")
        return False

    elif user == "N" or user == "n":
        user = input(f"Is the actual number greater than {mid}? (Y/N): ").strip()

        if user == "Y" or user == "y":
            return guessNumber(mid + 1, end)
        elif user == "N" or user == "n":
            return guessNumber(start, mid - 1)
        else:
            print("Please enter only Y or N")
            return guessNumber(start, end)

    else:
        print("Please enter only Y or N")
        return guessNumber(start, end)


print("Number Guessing Game in Python")

startRange = int(input("Enter Start Range: "))
endRange = int(input("Enter End Range: "))

print(f"Think of a number between {startRange} and {endRange}")
print("I will try to guess it!")

result = guessNumber(startRange, endRange)

if result:
    print("I couldn't guess your number.")
    print("Please answer correctly next time.")
