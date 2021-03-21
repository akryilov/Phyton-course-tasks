# Enter time in seconds
num_sec = int(input('Enter time in seconds: '))

#Calculate hours, minutes, seconds
hours = num_sec // 3600
minutes = (num_sec % 3600) // 60
seconds = (num_sec % 3600) % 60

#Print results, 2 variants for old and new Phyton versions:
print('Time in HH:MM:SS format: %02d:%02d:%02d ' % (hours, minutes, seconds))
print('Time in HH:MM:SS format: {:02}:{:02}:{:02} ' .format(hours, minutes, seconds))
