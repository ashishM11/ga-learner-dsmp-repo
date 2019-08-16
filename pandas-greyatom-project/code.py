# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
 # code starts here

bank = pd.read_csv(path,sep=',',header=0)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)


# code ends here


# --------------
# code starts here

banks  = bank.drop(columns='Loan_ID')

bank_mode = banks.mode()
all_cols = list(bank_mode.columns)

def get_data_frame(cols,banks):
    for col in cols:
        banks[col] = banks[col].fillna(bank_mode[col][0])
    return banks

banks = get_data_frame(all_cols,banks)

banks.info()


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

print(avg_loan_amount)
# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]

loan_status_count = len(banks['Loan_Status'])
loan_approved_se_count= len(loan_approved_se)
loan_approved_nse_count= len(loan_approved_nse)

percentage_se = (loan_approved_se_count / loan_status_count) * 100
print(percentage_se)
percentage_nse = (loan_approved_nse_count / loan_status_count) * 100
print(percentage_nse)
# code ends here


# --------------
# code starts here
def convert_loan_term_to_year(Loan_Amount_Term):
    return Loan_Amount_Term//12

loan_term = banks['Loan_Amount_Term'].apply(lambda x:convert_loan_term_to_year(x))

big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


