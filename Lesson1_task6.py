# Enter the first day distance 'a' and the control distance 'b'
a = float(input('Enter the first day distance: '))
b = int(input('Enter the control distance: '))
# n - number of days
n=1
if b > a:
    while b > a:
        a = a + (a * 0.1) # increase the distance at 10%
        n = n + 1 # increase the number of days
    print (f'The total number of days is: {n}')
else:
    print(f'The total number of days is: {n}')