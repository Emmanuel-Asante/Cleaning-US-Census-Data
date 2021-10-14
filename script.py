import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

# Inspect some of the csv files
print(pd.read_csv('states0.csv').head())
print(pd.read_csv('states1.csv').head())
print(pd.read_csv('states2.csv').head())

# Get all the csv files into a variable called files
files = glob.glob('states[0-9].csv')

# Create an empty list called files_list
files_list = []

# Loop through files
for filename in files:
  # Read all the csv files and append each of the file to files_list
  files_list.append(pd.read_csv(filename))

# Join all the csv files together and assign them to a DataFrame called us_census
us_census = pd.concat(files_list)

# Get the first five rows of us_census
print(us_census.head(10))

# Display the columns of us_census
print(us_census.columns)

# Display the dtypes of us_census
print(us_census.dtypes)

# Remove the dollar signs from each entry of the Income column
us_census.Income = us_census['Income'].replace('[\$]', '', regex = True)

# Convert the object type of the Income column to a numerical type (float64)
us_census.Income = pd.to_numeric(us_census.Income)

# Seperate GenderPop using regex
split_gender = us_census['GenderPop'].str.split('(\d+)', expand=True)

# 'Men' column
us_census['Men'] = split_gender.get(1)

# 'Women' column
us_census['Women'] = split_gender.get(3)

#  Convert the object type of the Men column to a numerical type
us_census.Men = pd.to_numeric(us_census.Men)

#  Convert the object type of the Women column to a numerical type
us_census.Women = pd.to_numeric(us_census.Women)

# Use matplotlib to make a scatterplot of the 'Women' column VS 'Income' column
plt.scatter(us_census['Women'], us_census['Income'])

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Examine the 'Women' column of us_census to check for nan values
print(us_census['Women'])

# Fill the 'nans' of the 'Women' column
us_census = us_census.fillna(
  value = {
    'Women': us_census.TotalPop - us_census.Men
  }
)

# Examine 'Women' column
print(us_census['Women'])

# Check for duplicates on us_census
print(us_census.duplicated(subset=['State']))

# Drop duplicates
us_census = us_census.drop_duplicates()

# Use matplotlib to make a scatterplot of the 'Women' column VS 'Income' column
plt.scatter(us_census['Women'], us_census['Income'], color=['red', 'green'])

# Lebel 'Women' on x-axis
plt.xlabel('Women')

# Lebel 'Income' on y-axis
plt.ylabel('Income')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Examine the columns of us_census
print(us_census.columns)

# Get the 'Hispanic' data without the '%' sign
us_census['Hispanic'] = us_census.Hispanic.str[:-1]

# Convert 'Hispanic' dtype to a numeric type of data
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)

# Get the 'White' data without the '%' sign
us_census['White'] = us_census.White.str[:-1]

# Convert 'White' dtype to a numeric type of data
us_census.White = pd.to_numeric(us_census.White)

# Get the 'Black' data without the '%' sign
us_census['Black'] = us_census.Black.str[:-1]

# Convert 'Black' dtype to a numeric type of data
us_census.Black = pd.to_numeric(us_census.Black)

# Get the 'Native' data without the '%' sign
us_census['Native'] = us_census.Native.str[:-1]

# Convert 'Native' dtype to a numeric type of data
us_census.Native = pd.to_numeric(us_census.Native)

# Get the 'Asian' data without the '%' sign
us_census['Asian'] = us_census.Asian.str[:-1]

# Convert 'Asian' dtype to a numeric type of data
us_census.Asian = pd.to_numeric(us_census.Asian)

# Get the 'Pacific' data without the '%' sign
us_census['Pacific'] = us_census.Pacific.str[:-1]

# Convert 'Pacific' dtype to a numeric type of data
us_census.Pacific = pd.to_numeric(us_census.Pacific)

# Fill nan values with the corresponding mean() aggregate value of each column data
us_census = us_census.fillna(
  value = {
    'Hispanic': us_census.Hispanic.mean(),
    'White': us_census.White.mean(),
    'Black': us_census.Black.mean(),
    'Native': us_census.Native.mean(),
    'Asian': us_census.Asian.mean(),
    'Pacific': us_census.Pacific.mean()
  }
)

# Check for duplicates on 'Hispanic' race
print(us_census['Hispanic'].duplicated().value_counts())

# Check for duplicates on 'White' race
print(us_census['White'].duplicated().value_counts())

# Check for duplicates on 'Black' race
print(us_census['Black'].duplicated().value_counts())

# Check for duplicates on 'Native' race
print(us_census['Native'].duplicated().value_counts())

# Check for duplicates on 'Asian' race
print(us_census['Asian'].duplicated().value_counts())

# Check for duplicates on 'Pacific' race
print(us_census['Pacific'].duplicated().value_counts())

# Drop 'Hispanic' column duplicates
us_census = us_census.drop_duplicates(subset=['Hispanic'])

# Drop 'White' column duplicates
us_census = us_census.drop_duplicates(subset=['White'])

# Drop 'Black' column duplicates
us_census = us_census.drop_duplicates(subset=['Black'])

# Drop 'Native' column duplicates
us_census = us_census.drop_duplicates(subset=['Native'])

# Drop 'Asian' column duplicates
us_census = us_census.drop_duplicates(subset=['Asian'])

# Drop 'Pacific' column duplicates
us_census = us_census.drop_duplicates(subset=['Pacific'])

# Check for duplicates on 'Hispanic', 'White', 'Black', 'Native', 'Asian' and 'Pacific' columns
print(us_census['Hispanic'].duplicated().value_counts())
print(us_census['White'].duplicated().value_counts())
print(us_census['Black'].duplicated().value_counts())
print(us_census['Native'].duplicated().value_counts())
print(us_census['Asian'].duplicated().value_counts())
print(us_census['Pacific'].duplicated().value_counts())

# Use matplotlib to make a histogram of the 'Hispanic' race
plt.hist(us_census['Hispanic'])

# Display 'Hispanic' as a title
plt.title('Hispanic')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Use matplotlib to make a histogram of the 'White' race
plt.hist(us_census['White'])

# Display 'White' as a title
plt.title('White')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Use matplotlib to make a histogram of the 'Black' race
plt.hist(us_census['Black'])

# Display 'Black' as a title
plt.title('Black')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Use matplotlib to make a histogram of the 'Native' race
plt.hist(us_census['Native'])

# Display 'Native' as a title
plt.title('Native')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Use matplotlib to make a histogram of the 'Asian' race
plt.hist(us_census['Asian'])

# Display 'Asian' as a title
plt.title('Asian')

# Display the graph
plt.show()

# Clear current axes
plt.cla()

# Use matplotlib to make a histogram of the 'Pacific' race
plt.hist(us_census['Pacific'])

# Display 'Pacific' as a title
plt.title('Pacific')

# Display the graph
plt.show()

# Clear current axes
plt.cla()