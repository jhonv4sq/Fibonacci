class sequence:

    def fibonacciRecursive(number):
        if number <= 1:
            return 1
        else:
            return sequence.fibonacciRecursive(number-1) + sequence.fibonacciRecursive(number-2)
    
    
    def fibonacci(limit):
        for number in range(limit):
            print(sequence.fibonacciRecursive(number))