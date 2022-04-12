
# vorud maqadir azla
print("Enter the first side of your triangle:")
side1 = input()
print("\nEnter the second side of your triangle:")
side2 = input()
print("\nEnter the third side of your triangle:")
side3 = input()

# check shart
if int(side1) < int(side2+side3) & int(side2) < int(side1+side3) & int(side3) < int(side1+side2):
    print("Your inputs are valid.")
else:
    print("You can't create a triangle with these amounts. try again.")
