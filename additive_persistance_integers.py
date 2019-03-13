def run():
    file_ = open("input.txt", "r")
    for line in file_:
        number = int(line.rstrip())
        result = additive_persistance(number)
        print "Input: %d" % (number)
        print "Itterations: %d" % (result)
        print "\n"
    file_.close()

def additive_persistance(number):
    '''
        Return the additive_persistance of the input.

        Args:
            number (int): The input value

        Returns:
            int: The additive_persistance of the input
    '''
    assert isinstance(number, int), "Input must be an Integer!"

    itterations = 0
    while number >= 10:
        number = sum_digits(number)
        itterations += 1
    return itterations

def sum_digits(number):
    '''
        Returns the sum of the digits of the input.

        Args:
            number (int): The input value

        Returns:
            int: The sum of the digits of the input
    '''
    assert isinstance(number, int), "Input must be an Integer!"

    sum_ = 0
    while number > 0:
        digit = number % 10
        sum_ += digit
        number /= 10
    return sum_


run()
