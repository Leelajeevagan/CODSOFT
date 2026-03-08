names = []
numbers = []

for i in range(3):
    name = input("Enter name: ")
    num = input("Enter number: ")

    names.append(name)
    numbers.append(num)

for i in range(len(names)):
    print(names[i],":",numbers[i])