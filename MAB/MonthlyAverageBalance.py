#!/usr/bin/env python
# coding: utf-8


# Import required libraries
from sympy.solvers import solve # to solve equation
from sympy import Symbol
import numpy as np
import math
import calendar
from datetime import date

today=date.today() # Today's date-time
day=today.day # Today's day of month
month=today.month # Today's month
year=today.year # Today's year
no_of_days=calendar.monthrange(year,month)[1] # Number of days in today's month

mab=float(input("Enter the Monthly Average Balance required to maintain: ")) # Monthly average balance required to maintaincurrent_mab=float(input("Enter your current Monthly Average Balance: ")) # Current MAB
current_bal=float(input("Enter your current Balance: ")) # Current balance

total_bal_req=mab*no_of_days # Total balance required to maintained (Sum of amount in account at EOD throughout the month)
total_maintained=current_mab*day # Total balance maintained till now (Sum of amount in account at EOD till now)
avg_to_maintain=(total_bal_req-total_maintained)/(no_of_days-day) # Average balance require to maintain to complate MAB

# print("Average balance need to maintain for Minimum Average Balance is: ",avg_to_maintain)
print("Average balance need to maintain for Minimum Average Balance is: ","%.2f" % round(avg_to_maintain,2))

money_to_add=float(input("Enter the amount which you want to deposit: ")) # Amount which you want to add extra
new_current_bal=current_bal+money_to_add # Current balance after adding extra amount

x=Symbol('x') # making x as a variable

# Number of days required to keep the extra amount to maintain the MAB 
days_to_keep_added_money=solve(((current_mab*day)+(new_current_bal*x)+(current_bal*(no_of_days-(day+x))))/no_of_days-mab,x)

print("No. of days you need to keep the added money to maintain Minimum Average Balance is: ",math.ceil(days_to_keep_added_money[0]))

