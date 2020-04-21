t = (0, 4, 132.42222, 10000, 12345.67)
n1 = t[0]
n2 = t[1]
number1 = round(t[2], 2)
number2 = "{:.2E}".format(t[3])
number3 = "{:.2E}".format(t[4])
print(f'day_0{n1}, ex_0{n2} : {number1}, {number2}, {number3}')
