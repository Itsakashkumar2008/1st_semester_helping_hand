num = int(input("enter your number: "))
if num == 0:
    print(0)
else:
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2                    
    print("Binary of your given number is :", binary)
