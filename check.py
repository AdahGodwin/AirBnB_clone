def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers.

    :param numbers: A list of numbers
    :return: The average of the numbers
    """
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

