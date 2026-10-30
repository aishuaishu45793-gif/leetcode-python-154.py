try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        digits = str(number)
        power = len(digits)
        total = 0

        for digit in digits:
            total += int(digit) ** power

        if total == number:
            print(number, "is an Armstrong number.")
        else:
            print(number, "is not an Armstrong number.")

except ValueError:
    print("Please enter a valid integer.")