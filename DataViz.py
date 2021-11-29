import csv
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Suspension_TeachExp_Finance.csv")
#dropping index column lol 
data = data.drop(columns = ["Unnamed: 0"])
