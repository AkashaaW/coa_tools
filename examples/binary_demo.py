from coa_tools.binary import to_binary, twos_complement, from_binary

choice = input("1: Decimal to binary, 2: Binary to decimal: ")
text = input("Enter your number: ")

try:
    if choice == "1":
        number = int(text)
        if number < 0:
            print(twos_complement(number))
        else:
            print(to_binary(number))
    elif choice == "2":
        print(from_binary(text))
    else:
        print("Please choose 1 or 2.")
except ValueError as error:
    print(f"Invalid input: {error}")