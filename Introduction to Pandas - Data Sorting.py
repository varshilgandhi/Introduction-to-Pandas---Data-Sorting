# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 06:19:51 2021

@author: abc
"""
 

#soring one columns in ascending order
#here by default order is ascending 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df2 = df.sort_values('Manual',ascending=True) 
print(df2['Manual'])



###########################################################################

#print subsets

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

print(df[20:30])                  #It's print all columns between 20 to 30 rows 
print(df.loc[20:30, ['Manual', 'Auto_th_2']])  #It's only two columns between 20 to 30 rows

 

###########################################################################

#Select rows using row values

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

set2_df = df[df['Unnamed: 0'] == 'Set2']
print(set2_df)      #It's Print all the values of set2

print(max(set2_df['Manual']))    #It's print the maximum value of manual column of set2

print(min(set2_df['Manual']))    #It's print the minimum value of manual column of set2


##############################################################################

#find the values which is greater than 100

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

print(df['Manual'])
print(df['Manual'] > 100.)     #It's print the values that greater than 100 in the manner of true and false

print(df[df['Manual'] > 100.])  #It's print the values that greater than 100 in numbers :

print(df[(df['Manual'] > 100.) & (df['Auto_th_2'] < 100.)]) #It's print Manual value > 100 
                                                             # and Auto_th_2 value < 100


############################################################################################

#Iteration Concept 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

for index, row in df.iterrows():
    average_auto = (row['Auto_th_2'] + row['Auto_th_3'] + row['Auto_th_4']) / 3
    print(round(average_auto), row['Manual'])
    

####################################################################################

                #THANK YOU
                #TAKE CARE BE SAFE FROM CORONA
                #TWO GAJJ KI DURII HEE JARURI


















