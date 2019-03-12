f = open("input.txt", "r")
for line in f:
    additive_persistance(line)
f.close()

#Return the additive_persistance of the input
#Precondition: number is of type String
def additive_persistance(number):
    assert type(number) == type("str"), "Input must be a String!"
    itterations = 0
    while len(number) > 1:
        number = sum_digits(number)
        itterations += 1
    return itterations

#Return the sum of digits of the input
#Precondition: number is of type String
def sum_digits(number):
    assert type(number) == type("str"), "Input must be a String!"
    return sum([int(char) for char in number])
