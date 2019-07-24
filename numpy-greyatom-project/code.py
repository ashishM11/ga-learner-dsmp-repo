# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
new_census_record = np.array(new_record)
census = np.concatenate((data,new_census_record), axis=0)
print("\nData: \n\n", census)


# --------------
#Code starts here

age  = census[0:,0]
print(age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here

def get_subset_array(race_type):
    census_cond = census[:,2] == race_type
    return census[census_cond]


race_0 = get_subset_array(0)
race_1 = get_subset_array(1)
race_2 = get_subset_array(2)
race_3 = get_subset_array(3)
race_4 = get_subset_array(4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 3




# --------------
#Code starts here

senior_citizens_cond = census[:,0] > 60
senior_citizens = census[senior_citizens_cond]

working_hours_sum = np.sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len

print(avg_working_hours)



# --------------
#Code starts here
high_edu_cond = census[:,1] > 10
low_edu_cond = census[:,1] <= 10

high = census[high_edu_cond]
low = census[low_edu_cond]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


