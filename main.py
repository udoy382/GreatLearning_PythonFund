def prog():
    msg1 = """
    Select which program you want to use:
    [1] - Even or Odd - Check even or odd number
    [2] - Text uppercase and lowercase converter - Convert your text to uppercase or lowercase letter.
    [3] - Calculator - Calculate any number
    """
    print(msg1)
    user1 = int(input("Enter number here > "))
    if user1 == 1:
        try:
            user2 = int(input("Enter you number for check even or odd number > "))
            if user2 % 2 == 0:
                print("This is a Even number")
            else:
                print("This is a Odd number")
        except Exception:
            print("Oops! something wrong. Please try again.")
    elif user1 == 2:
        msg2 = """
        [1] - Uppercase
        [2] - Lowercase
        """
        print(msg2)
        n1 = int(input("Enter your option > "))
        try:
            if n1 == 1:
                user3 = str(input("Enter your text here for uppercase convert > "))
                for text in user3:
                    print(text.upper())
            elif n1 == 2:
                user3 = str(input("Enter your text here for lowercase convert > "))
                for text in user3:
                    print(text.lower())
        except Exception:
            print("Oops! something wrong. Please try again.")
    elif user1 == 3:
        try: 
            first_number = int(input("Enter your first number > "))
            op = input("Enter operator > ")
            second_number = int(input("Enter your second number > "))
            if op == "+":
                print(first_number + second_number)
            elif op == "-":
                print(first_number - second_number)
            elif op == "*":
                print(first_number * second_number)
            elif op == "**":
                print(first_number ** second_number)
            elif op == "/":
                print(first_number / second_number)
            elif op == "//":
                print(first_number // second_number)
            else:
                print("something problem, try agian.")
        except Exception:
            print("Oops! something wrong. Please try again.")

prog()