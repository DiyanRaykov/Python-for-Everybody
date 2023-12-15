hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = 0

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
def computepay(hrs1, rate1):
    if hrs1 > 40:
        extra_hrs = hrs1 - 40
        over_pay = extra_hrs * rate1 * 1.5
        pay1 = (hrs1 - extra_hrs) * rate1 + over_pay
    else:
        pay1 = hrs1 * rate1
    return pay1

pay = computepay(hrs, rate)
print(f"Pay {pay:.2f}")
