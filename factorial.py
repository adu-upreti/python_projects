


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)



def factorialTrailingZeros(number):
    count = 0
    i = 5 

    while(number//i !=0):
        count += int(number/i)
        i = i*5
        return count




number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial_recursive(number)}")
print(f"The factorial trailling zero in {number} is {factorialTrailingZeros(number)}")






# import time
# start = time.time()
# end = time.time()
# execution_time = end - start 
# print(f"execution time is {execution_time}")