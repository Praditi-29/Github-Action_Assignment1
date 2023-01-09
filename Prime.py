import os
start= int(os.environ["num1"]) 
end= int(os.environ["num2"]) 
print("Prime numbers are:")
for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            print(num)