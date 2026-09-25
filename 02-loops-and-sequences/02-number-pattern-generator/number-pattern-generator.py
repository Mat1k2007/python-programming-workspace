def number_pattern(n):
    result = []
    
    # Type validation
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    
    # Boundary check
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    # Sequence generation using for loop
    for number in range(1, n + 1):
        result.append(str(number))
        
    return ' '.join(result)


# Test cases
if __name__ == "__main__":
    print(number_pattern(4))      # Output: "1 2 3 4"
    print(number_pattern("test")) # Output: "Argument must be an integer value."
    print(number_pattern(0))      # Output: "Argument must be an integer greater than 0."