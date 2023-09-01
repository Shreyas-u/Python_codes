def sum_of_multiples(limit):
    result = 0
    for num in range(limit + 1):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result

# Example usage:
limit = int(input("Enter the limit: "))
total_sum = sum_of_multiples(limit)
print(f"The sum of multiples of 3 and 5 between 0 and {limit} is: {total_sum}")

