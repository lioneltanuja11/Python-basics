# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:34:53 2024

@author: kruth
"""

#def pattern6():
# n = int(input('Enter a num:'))
 #for i in range(1,n+1):
  #   print(' '*(n-i),'*'*(i+(i-1)))
#pattern6()
     
def pattern6():
 n = int(input('Enter a num:'))
 for i in range(n,0,-1):
     print(' '*(n-i),'*'*(i+(i-1)))
pattern6()
     