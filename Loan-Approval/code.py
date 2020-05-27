# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
print(bank_data.shape)


#Code starts here
categorial_var = bank_data.select_dtypes(include = 'object')
#print(categorial_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
#print(numerical_var.shape)

banks = bank_data.drop(['Loan_ID'] , axis = 1)
print(banks.shape)
#print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
#print(banks.isnull().sum().values.sum())
banks.fillna(bank_mode , inplace = True)
print(banks.isnull().sum().values.sum())
avg_loan_amount = pd.pivot_table(banks , index = ['Gender' , 'Married' , 'Self_Employed'] , values = 'LoanAmount' , aggfunc = 'mean')
#print(avg_loan_amount)
print(round(avg_loan_amount['LoanAmount'][1],2))

loan_approved_se = banks[banks['Self_Employed'] == 'Yes']
loan_approved_se = len(loan_approved_se[loan_approved_se['Loan_Status'] == 'Y'])

loan_approved_nse = banks[banks['Self_Employed'] == 'No']
loan_approved_nse = len(loan_approved_nse[loan_approved_nse['Loan_Status'] == 'Y'])

Loan_Status = len(banks)
print(Loan_Status)

percentage_se = round((loan_approved_se/Loan_Status)*100 , 2)
print(percentage_se)

percentage_nse = round((loan_approved_nse/Loan_Status)*100 , 2)
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x / 12)
big_loan_term = len(list(filter(lambda x : x >= 25 , loan_term)))
print(big_loan_term)

loan_groupby = banks[['ApplicantIncome','Credit_History' , 'Loan_Status']]
mean_values = loan_groupby.groupby('Loan_Status').mean()

print(round(mean_values.iloc[1,0] , 2))




