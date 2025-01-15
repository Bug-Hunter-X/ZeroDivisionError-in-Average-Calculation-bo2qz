def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list explicitly
    return sum(numbers) / len(numbers)

# Example usage
my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1, 0, 3, 0, 5]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average of list with zeros is: {average_with_zero}") 