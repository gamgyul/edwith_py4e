def calc_payroll(a_hours, a_rate):
    try:
        hours = int(a_hours)
        rate = float(a_rate)
    except:
        print('Error, please enter numeric input')
        quit()
    base_pay =hours * rate
    if hours > 40:
        bonus = (hours-40) * rate * 0.5
        pay = base_pay + bonus
    else:
        pay= base_pay

    print('Pay:', pay)

calc_payroll(10,10)