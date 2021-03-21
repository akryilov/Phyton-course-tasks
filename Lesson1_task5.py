# Enter the value of proceeds
pros = int(input('Enter the proceeds value: '))
# Enter the value of costs
cost = int(input('Enter the costs value: '))
# Results calculation
if pros > cost:
    print('Work with profit')
    # Profitability calculation
    prof = (pros - cost) / pros
    print(f'Profitability is: {prof}')
    # Profit per employee calculation
    empnum=int(input('Enter the number of employees: '))
    print(f'Profit per employee is: {(pros - cost) / empnum}')
else:
    print('Work with losses')
