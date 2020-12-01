# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
import time
argv = sys.argv[1:4]

if 'h' in argv or 'help' in argv:
    print('Enter WORKING HOURS, RATE PER HOUR, BONUS using space \n'
          'SALARY will be calculated as result')

if len(argv) == 3:
    print(f'Calculating you salary... \nPlease wait')
    time.sleep(2)
    print(f'SALARY IS: {int(argv[0]) * int(argv[1]) + int(argv[2])} $')
else:
    print('Error!')