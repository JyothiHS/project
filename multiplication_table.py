# -*- coding: utf-8 -*-
"""multiplication_table.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dEasyMKGUS3Q-gEZx7ZE3Bv60FGWvDGO
"""

user_num = int(input("Enter the number you want to generatate a multiplication table :"))
Range = range(1,11)
for x in Range:
    result = user_num * x
    print(user_num," * ",x," = ",result)

