credit_hours = 1
district = 'homeschool'
out_of_state = True

dual_fee_exemption = ['hampton', 'jasper', 'polaris']
dual_fee_waiver_list_2 = ['homeschool', 'private', 'other']

print('--------------------------')
lottery_tuition_assistance = 85
lottery_tuition_assistance_total = 0

esser_fund = 75
esser_fund_total = 0

dual_fee_waiver_beaufort = 31
dual_fee_waiver_homeschool_private_other = 41
dual_fee_total = 0

if out_of_state:
    print('Exempt from lottery because out of state.')
    state_string = 'out of'
elif credit_hours > 5:
    lottery_tuition_assistance_total += credit_hours * lottery_tuition_assistance
    state_string = 'in'
elif credit_hours < 6:
    print('Not enough credit hours for lottery tuition.')
    state_string = 'in'


if district in dual_fee_waiver_list_2:
    print(f'No esser assistance because distract was {district}.')
    pass
elif district == 'beaufort':
    esser_fund_total += credit_hours * esser_fund
elif district in dual_fee_exemption:
    pass

if district in dual_fee_exemption:
    print(f'dual fee was exempted because district was {district}.')

elif district == 'beaufort':
    dual_fee_total += credit_hours * dual_fee_waiver_beaufort
    print('dual fee was in beaufort.')

elif district in dual_fee_waiver_list_2:
    dual_fee_total += credit_hours * dual_fee_waiver_homeschool_private_other
    print(f'dual fee was in {dual_fee_waiver_list_2}.')

else:
    print('MISSPELLING!!!')

total_assistance = lottery_tuition_assistance_total + esser_fund_total + dual_fee_total

if esser_fund_total == 0 and district in dual_fee_exemption:
    esser_fund_total = 'covering the rest of tuition'


print(f'Student is {state_string} state')

print(f'''
Student's total credit hours are {credit_hours}.
Total assistance is {total_assistance}.
Lottery tuition assistance is {lottery_tuition_assistance_total}.
Esser assistance is {esser_fund_total}.
Dual fee waiver assistance is {dual_fee_total}.
''')

