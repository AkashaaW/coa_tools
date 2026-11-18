from coa_tools.binary import to_binary
from coa_tools.binary import twos_complement

number = int(input("Enter a decimal integer: "))
if number < 0:
    print(twos_complement(number))
else: 
    print(to_binary(number))

