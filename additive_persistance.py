def run():
    file_ = open("input.txt", "r")
    for line in file_:
        number = line.rstrip()
        result = additive_persistance(number)
        print "Input: %s" % (number)
        print "Itterations: %s" % (result)
        print "\n"
    file_.close()

def additive_persistance(number):
    '''
        Return the additive_persistance of the input.

        Args:
            number (str): The input value

        Returns:
            str: The additive_persistance of the input
    '''
    assert type(number) == type("str"), "Input must be a String!"

    itterations = 0
    while len(number) > 1:
        number = sum_digits(number)
        itterations += 1
    return itterations

def sum_digits(number):
    '''
        Returns the sum of the digits of the input.

        Args:
            number (str): The input value

        Returns:
            str: The sum of the digits of the input
    '''
    assert type(number) == type("str"), "Input must be a String!"

    sum_ = 0
    for digit in number:
        sum_ += int(digit)
    return str(sum_)


run()
