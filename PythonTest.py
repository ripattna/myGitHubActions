""" File contains various function to under Pylint """


def is_number_even(num):
    """Function to check if number is even or odd"""
    return "Even" if num % 2 == 0 else "Odd"


NUM = 5
print(f"The number {NUM} is {is_number_even(NUM)}")
