time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time_string.split(',')
total_minutes = 0

for time in time_list:
    time = time.replace(' ', '')
    hours = 0
    minutes = 0
    seconds = 0

    if 'h' in time:
        hours = int(time[:time.index('h')])
        time = time[time.index('h') + 1:]
    if 'm' in time:
        minutes = int(time[:time.index('m')])
        time = time[time.index('m') + 1:]
    if 's' in time:
        seconds = int(time[:time.index('s')])

    total_minutes += hours * 60 + minutes + seconds / 60

print(int(total_minutes))