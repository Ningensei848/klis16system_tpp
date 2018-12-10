# -*- encoding: utf-8 -*-

import sys

args = sys.argv

#print(type(args)) # <class 'list'>


##################### Convenient Function for Reduce ##################################

# fの総数を指定
number = int(args[1])

# すでに存在する（計算が済んだ）範囲の最大のfを指定
used_number = int(args[2])

# Define some functions

def make_list(number):
  temp_list = []
  
  for var in range(0, number):
    var += 1
    temp_str = 'f' + str(var)
    temp_list.append(temp_str)
  #print(temp_list)
  
  return temp_list
    

    
def make_gspoly(n1, n2):
  print('s{}{}'.format(n1, n2) + ':=gspoly(f{}, f{});'.format(n1, n2))
  
    
def make_preduce(n1, n2, g_list):  
    temp_str = ""
    for func in g_list:
        temp_str += func + ", "
    temp_str = "{" + temp_str[:-2] + "}"
    print('preduce(s{}{}, '.format(n1, n2) + temp_str + ');')

g_list = make_list(number)

for j in range(1, number):
    for k in range(0, number):
        k += 1
        if k <= used_number or j >= k:
            continue
        else:  
            make_gspoly(j, k)
            make_preduce(j, k, g_list)