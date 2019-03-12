#Return the additive_persistance of the input
#Precondition: number is of type String
def additive_persistance(number):
    assert type(number) == type("str"), "Input must be a String!"
    
    itterations = 0
    while len(number) > 1:
        number = sum_digits(number)
        itterations += 1
    return itterations

#Return the sum of digits of the input as a String
#Precondition: number is of type String
def sum_digits(number):
    assert type(number) == type("str"), "Input must be a String!"
    
    _sum = 0
    for i in range(len(number)):
        _sum += int(number[i])
    return str(_sum)

def run():
    f = open("input.txt", "r")
    for line in f:
        result = additive_persistance(line.rstrip())
        print "\nInput: %s \nItterations: %s" % (line.rstrip(), result)
    f.close()

run()
