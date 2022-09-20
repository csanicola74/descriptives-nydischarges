# Import packages
from statsmodels.formula.api import ols
import pandas
import scipy
from scipy import stats
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.express as px
import urllib.request
import os
import seaborn

###############################
##  Reading from a CSV file  ##
###############################

sparcs = pandas.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

#########################
##  Manipulating data  ##
#########################

sparcs.shape    # 1000 rows and 34 columns
sparcs.columns
sparcs.dtypes
