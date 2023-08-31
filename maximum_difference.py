def find_difference(numbers):
    if not numbers:
        return 0

    max_num = max(numbers)
    min_num = min(numbers)

    return max_num - min_num

input_list = input("Enter a list of integers separated by spaces: ").split()

try:
    numbers = [int(num) for num in input_list]
    result = find_difference(numbers)
    print(f"The difference between the largest and smallest integers is: {result}")
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")
