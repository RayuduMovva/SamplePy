from sample_calculator import Calculator


def main():
    print("Hello from samplepy!")
    
    # Create an instance of the Calculator class
    calc = Calculator()
    
    # Call the add_numbers method
    result = calc.add_numbers(5, 3)
    print(f"The sum is: {result}")

    # Example usage with the object
    result_add = calc.add_numbers(5, 3)
    print(f"The sum is: {result_add}")

    result_sub = calc.subtract_numbers(5, 3)
    print(f"The difference is: {result_sub}")

    result_mul = calc.multiply_numbers(5, 3)
    print(f"The product is: {result_mul}")

    result_div = calc.divide_numbers(5, 3)
    print(f"The quotient is: {result_div}")

if __name__ == "__main__":
    main()
