# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
additional_amount = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
current_month = 0

while principal > 0:
    current_month = current_month + 1
    if extra_payment_start_month <= current_month <= extra_payment_end_month:
        effective_payment = payment + additional_amount
    else:
        effective_payment = payment

    principal = principal * (1 + rate / 12) - effective_payment
    if principal < 0:
        effective_payment = 0 - principal
        principal = 0
    total_paid = total_paid + effective_payment
    print(current_month, round(effective_payment, 2), round(principal, 2))

print('Total paid', total_paid)
print('Month', current_month)
