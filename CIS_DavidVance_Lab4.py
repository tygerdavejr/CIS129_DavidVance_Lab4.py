# CIS129_DavidVance_Lab4.py
"""Determine total bonuses based off store and individual sales."""
# David Vance
# Professor Kevin Chang
# CIS-129 Programming and Problem Solving
# 19 September 2024

# This program determines employee bonuses based on the amount of
# sales both the store and the individual do in one month.

# Declare local variables
monthly_sales_amount = 0  # monthly sales amount
store_bonus_amount = 0  # store bonus amount
employee_bonus_amount = 0  # employee bonus amount
sales_increase = 0  # percent of sales increase
prompt = 'Enter the monthly sales $' # prompt will be a string literal


# This code gets the monthly sales
monthly_sales_amount = float(input(prompt))

# This code determines the store bonus

# Student Note: The lab's pseudocode does not match the program description.
# The $6000 bonus is awarded if monthly sales are GREATER THAN $110,000.
# The pseudocode used >=.

if monthly_sales_amount >= 110000:
	store_bonus_amount = 6000
elif monthly_sales_amount >= 100000:
	store_bonus_amount = 5000
elif monthly_sales_amount >= 90000:
	store_bonus_amount = 4000
elif monthly_sales_amount >= 80000:
	store_bonus_amount = 3000
else:
	store_bonus_amount = 0


# This code gets the percent of increase in sales
prompt = 'Enter percent of sales increase: '  # This was not in the supplied pseudocode
sales_increase = float(input(prompt)) # I could have changed this but they wanted a prompt variable
sales_increase = sales_increase / 100


# This code determines the employee bonus
if sales_increase >= .05:
	employee_bonus_amount = 75
elif sales_increase >= .04:
	employee_bonus_amount = 50
elif sales_increase >= .03:
	employee_bonus_amount = 40
else:
	employee_bonus_amount = 0

# This code prints the bonus information
print("The store bonus amount is $", store_bonus_amount)
print("The employee bonus amount is $", employee_bonus_amount)
if (store_bonus_amount == 6000 ) and (employee_bonus_amount == 75):
	print('Congrats! You have reached the highest bonus amounts possible! ')
