def function_with_uncommon_error(x, y):
    try:
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise TypeError("Inputs must be numbers")
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_uncommon_error(10, "hello") # Output: Error: Inputs must be numbers, None
result4 = function_with_uncommon_error(10, 2.5) # Output: 4.0
result5 = function_with_uncommon_error("hello",2) # Output: Error: Inputs must be numbers, None