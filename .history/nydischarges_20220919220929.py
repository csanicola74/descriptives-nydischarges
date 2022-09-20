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
from tableone import TableOne, load_dataset

###############################
##  Reading from a CSV file  ##
###############################

sparcs = pandas.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
sparcs

#########################
##  Manipulating data  ##
#########################

sparcs.shape    # 1000 rows and 34 columns
sparcs.columns
sparcs.dtypes
# health_service_area                     object
# hospital_county                         object
# operating_certificate_number           float64
# facility_id                            float64
# facility_name                           object
# age_group                               object
# zip_code_3_digits                       object
# gender                                  object
# race                                    object
# ethnicity                               object
# length_of_stay                           int64
# type_of_admission                       object
# patient_disposition                     object
# discharge_year                           int64
# ccs_diagnosis_code                       int64
# ccs_diagnosis_description               object
# ccs_procedure_code                       int64
# ccs_procedure_description               object
# apr_drg_code                             int64
# apr_drg_description                     object
#  apr_mdc_code                             int64
# apr_mdc_description                     object
# apr_severity_of_illness_code             int64
# apr_severity_of_illness_description     object
# apr_risk_of_mortality                   object
# apr_medical_surgical_description        object
# payment_typology_1                      object
# payment_typology_2                      object
# payment_typology_3                      object
# birth_weight                             int64
# abortion_edit_indicator                 object
# emergency_department_indicator          object
# total_charges                          float64
# total_costs                            float64

##############################
##  Full Dataframe Measure  ##
##############################

sparcs.mean()
sparcs.var()
sparcs.describe()

######################################################################
##  Categorical variables: comparing groups or multiple categories  ##
######################################################################

# seeing the relationship between age group and diagnosis code
age_diag = ols("ccs_diagnosis_code ~ age_group + 1", sparcs).fit()
print(age_diag.summary())

# seeing the relationship between length of stay and severity of illness
stay_illness = ols(
    "length_of_stay ~ apr_severity_of_illness_code + 1", sparcs).fit()
print(stay_illness.summary())

# a correlation coefficient with scipy.stats.linregress():
scipy.stats.linregress(sparcs['length_of_stay'],
                       sparcs['apr_severity_of_illness_code'])

###############
##  TableOne ##
###############

### DATASET 1 ###
sparcs_df1 = sparcs.copy()
sparcs_df1.dtypes
list(sparcs_df1)

sparcs_df1_columns = ['length_of_stay',
                      'ccs_diagnosis_code',
                      'ccs_procedure_code',
                      'apr_severity_of_illness_code',
                      'total_charges']


#######################
##  Visualizing Data ##
#######################

# Now that you have the data to work with, you can apply .boxplot() to get the box plot:
fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()
