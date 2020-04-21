def format_number(number):
    return '0' + str(number) if number < 10 else number


t = (3, 30, 2019, 9, 25)
day = format_number(t[4])
month = format_number(t[3])
year = format_number(t[2])
hour = format_number(t[0])
minute = format_number(t[1])
print(f'{month}/{day}/{year} {hour}:{minute}')
