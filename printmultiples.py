#Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7. I chave changed it to user input multiple number.

multiplenum = int(input("Enter the number for the multiples of:"))
for x in range(0,100):
    if x%multiplenum == 0:
        print(x)
