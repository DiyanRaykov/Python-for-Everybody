hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
# over_pay = 0

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if float(hrs) > 40:
    extra_hrs = hrs - 40
    over_pay = extra_hrs * rate * 1.5
    pay = (hrs - extra_hrs) * rate + over_pay
else:
    pay = hrs * rate

print(f"{pay:.2f}")
