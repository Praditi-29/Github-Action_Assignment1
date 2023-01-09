import sys

start=int(sys.argv[1])
end=int(sys.argv[2])
print('Prime Numbers are :')
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)