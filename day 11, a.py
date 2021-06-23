import day11_module as m
m.Greetings("Bernice")

import pandas as pd
a =[1,2,3,4]
series = pd.Series(a)
print("Series : \n",series)
print("Version of Pandas used : ",pd.__version__)

import random as rd
r = rd.randint(0,100)
print("Random number : ",r)

import sys
print("Path : \n",sys.path)
