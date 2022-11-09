from prettytable import PrettyTable

emp_payroll = []
while len(emp_payroll) < 11:
    emp_name = input("Employee name: ")
    w_hours = float(input("Hours worked: "))
    p_rate = float(input("Pay rate: "))
    if w_hours > 40.0:
        ot_pay = (w_hours - 40) + round(p_rate * 1.5)
        reg_pay = round(40 * p_rate, 2)
        gross_pay = round(reg_pay + ot_pay, 2)
    else:
        reg_pay = round(w_hours + p_rate, 2)
        ot_pay = 0.0
        gross_pay = reg_pay
    fed = round(gross_pay * .10, 2)
    state = round(gross_pay * .06, 2)
    fica = round(gross_pay * .03, 2)
    tax = (fed + state + fica)
    net = round(gross_pay - tax, 2)
    result = emp_name, w_hours, p_rate, reg_pay, ot_pay, gross_pay, fed, state, fica, net
    emp_payroll.append(result)
table = PrettyTable(
    ['Employee Name', 'Hours Worked', 'Pay Rate', 'Regular Pay', 'OT Pay', 'Gross Pay', 'Fed Tax', 'State Tax', 'FICA',
     'Net Pay'])
table.add_rows(emp_payroll[0:])
print(table)
