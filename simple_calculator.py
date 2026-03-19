#Calculator v3 (Menu Based)

while True:
    print("\n--- Simple calculator---")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice (1/2/3/4):")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == "1":
        print("Answer is:", num1+num2)
    elif choice == "2":
        print("Answer is:", num1-num2)
    elif choice == "3":
        print("Answer is:", num1*num2)
    elif choice == "4":
         if num2 != 0:
           print("Answer is:", num1/num2)
        
         else:
            print("Error: Division by zero is not possible.")
    else:
        print("Invalid choice")

        again = input("Do you want to continue? (yes/no):")
        if again.lower() != "yes":
            print("Calculator closed")
            break