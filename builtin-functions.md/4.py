import math
import time

time_miliseconds=int(input("Enter  miliseconds:"))/1000
number = int(input("number of square root ;"))
time.sleep(time_miliseconds)
print(f"Square root of {number} after {time_miliseconds} miliseconds is {math.sqrt(number)}")


