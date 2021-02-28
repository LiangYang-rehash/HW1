#!/usr/bin/env python
# coding: utf-8

# # calculating_the_bill

# You are asked to develop a Python program that calculates tip and total bill for a restaurant. Upon running the program, it asks the user:
# How much is your original bill?
# What percentage is your tip?
# The program takes the original bill amount as an input to calculate tip and total bill. Tip is based on the desired percentage of the original bill. It outputs
# Your tip based on __% is   ______ (fill in tip % and tip amount here)
# Your total bill is ___________ (fill in total bill here)
# 
# *Name your program Problem1_Lastname.py and submit it on Blackboard. Also submit a screenshot of your output result in the word document. 
# 

# In[1]:


original_bill = input('please enter: How much is your original bill? ')
tip_percentage = input('please enter: What percentage is your tip? ')
tip = float(original_bill) * float(tip_percentage) / 100
total_bill = tip + float(original_bill)
print('Your tip based on', tip_percentage, '% is', tip )
print('Your total bill is', total_bill)


# In[ ]:





# In[ ]:





# In[ ]:




