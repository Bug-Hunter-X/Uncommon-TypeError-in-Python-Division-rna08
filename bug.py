def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_uncommon_error(10, "hello") # Output: Error: Invalid input types, None
result4 = function_with_uncommon_error(10, 2.5)