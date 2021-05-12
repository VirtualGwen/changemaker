total_change = int(input())

if total_change <= 0:
    print('No change')

dollar = total_change // 100
total_change %= 100
quarter = total_change // 25
total_change %= 25
dime = total_change // 10
total_change %= 10
nickel = total_change // 5
total_change %= 5
penny = total_change % 5

if ((dollar > 0) and (dollar == 1)):
    print('{} Dollar'.format(dollar))
elif (dollar > 0):
    print('{} Dollars'.format(dollar))
if ((quarter > 0) and (quarter == 1)):
    print('1 Quarter')
elif (quarter > 0):
    print('{} Quarters'.format(quarter))
if ((dime > 0) and (dime == 1)):
    print('1 Dime')
elif (dime > 0):
    print('{} Dimes'.format(dime))
if (nickel == 1):
    print('1 Nickel')
elif (nickel > 0):
    print('{} Nickels'.format(nickel))
if (penny == 1):
    print('1 Penny')
elif (penny > 0):
    print('{} Pennies')
