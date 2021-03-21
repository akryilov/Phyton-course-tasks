# Enter the positive integer value 'n'
n = int(input('Enter the positive integer number: '))
m = n % 10
n = n // 10
# Finding the maximum number
while n > 0:
    #Condition check
    if n % 10 > m:
        m = n % 10
    n = n // 10
#Print the result
print(f'The maximum number is: {m}')