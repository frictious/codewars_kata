'''Create a function named divisors/Divisors that takes an integer n > 1
and returns an array with all of the integer's divisors(except for 1
and the number itself), from smallest to largest. If the number is
prime return the string '(integer) is prime' (null in C#) (use
Either String a in Haskell and Result<Vec<u32>, String> in Rust).'''
def divisors(integer):
    arr = [] #Creating an empty array to hold the values in later
    
    for divisor in range(2, integer + 1): # Looping from 2 to the number entered
        if integer % divisor == 0 and integer != divisor: # Condition to check if the value is completely divisible and not equal to the divisor
            arr.append(divisor) # Adding the factor to the array
    
    if len(arr) == 0: # Checking if the array does not have any value to check if it is a prime number
        for check in range(0, integer + 1):
            count = 0
            for prime in range(1, check + 1):
                if check % prime == 0:
                    count += 1

            if count == 2:
                return f"{integer} is a prime" # Returning the string if the value is a prime number
    else:
        return arr # Returning the array
