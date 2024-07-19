sum = 0
while True:
    userinput = input("Enter the product price or press q to quit: \n")
    if userinput != 'q':
        sum = sum + int(userinput)
        print(f"oredr total so far : {sum}")

    else: 
        print(f"total amount of your bill is {sum}.")
        break