# # Example: showing frequency of values
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import requests 



# # num = np.arange(1,11)
# # mean_num = np.mean(num)
# # print("Mean of numbers:", mean_num)

# # summary_stats = {
# #     'stud_chosen': ['SAndra', 'Collins', 'Steve'],
# #     'position': ['Leader', 'Member', 'Member']

# # }

# # df = pd.DataFrame(summary_stats)
# # print(df)


# # response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# # if response.status_code == 200:
# #     user_data = response.json()
# #     print("User Data:")
# #     print(user_data)
# # else:
# #     print("Failed to retrieve user data")

# # numbers = [1, 3, 2, 5, 7, 4]
# # plt.plot(numbers, marker='o')
# # plt.title('Simple Line Graph')
# # plt.xlabel('Index')
# # plt.ylabel('Value')
# # plt.grid(True)
# # plt.show()

# # # data = {
# # #     'Country' : ['kenya', 'Nigeria', 'Tanzania'],
# # #     'Population' : [34.5, 50.7, 89.4]
# # # }

# # # df = pd.DataFrame(data)

# # # # plt.bar(df['Country'], df['Population'])
# # # # plt.plot(df['Country'], df['Population'], marker='o')
# # # plt.pie(df['Population'], labels=df['Country'], autopct='%1.1f%%')
# # # plt.title("Population of countries")
# # # plt.xlabel("Country")
# # # plt.ylabel("Population in millions")
# # # plt.grid(True)
# # # plt.show()

# # # activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
# # # hours = [8, 2, 8, 6]

# # # plt.pie(hours, labels=activities, autopct='%1.1f%%')
# # # plt.title("Daily Activities")
# # # plt.show()



# # # import pandas as pd
# # # data = {
# # #     'Name' : ['Sandra', 'Collins', 'Steve'],
# # #     'Age' : [21, 19, 23],
# # #     'Score' : [90,85, 100]

# # # }
# # # df = pd.DataFrame(data)
# # # df['passed'] = df['Score'] >50
# # # print(f"Students who have passed , {df['passed']}")


# # # import numpy as np

# # # num = np.arange(10, 51)

# # # max_value = np.max(num)
# # # min_value = np.min(num)

# # # # Multiply all elements by 3
# # # multiplied = num * 3

# # # print("Maximum value:", max_value)
# # # print("Minimum value:", min_value)
# # # print("Multiplied by 3:", multiplied)

# # # max_value = max(num)
# # # min_value= min(num)


# # # multiplied = [x * 3 for x in num]

# # # print(num)
# # # print(max_value)
# # # print(min_value)
# # # print(multiplied)


import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Load and Explore the Dataset
# try:
#     df = sns.load_dataset('tips')
#     print("Tips dataset loaded successfully.\n")
# except Exception as e:
#     print(f"Error loading dataset: {e}")
#     exit()

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean the dataset (fill missing values if any)
if df.isnull().values.any():
    df = df.fillna(df.mean(numeric_only=True))
    print("\nMissing values filled with column mean.")
else:
    print("\nNo missing values found.")

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

# Group by 'sex' and compute mean of 'total_bill'
grouped = df.groupby('sex')['total_bill'].mean()
print("\nMean total bill per sex:")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart: total_bill trend across samples
plt.plot(df.index, df['total_bill'], label='Total Bill')
plt.title('Total Bill Trend Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Total Bill')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar chart: Average total bill per sex
plt.bar(grouped.index, grouped.values)
plt.title('Average Total Bill per Sex')
plt.xlabel('Sex')
plt.ylabel('Average Total Bill')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of total bill
plt.hist(df['total_bill'], bins=20, color='skyblue')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter plot: Total bill vs tip
plt.scatter(df['total_bill'], df['tip'], c=df['size'])
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.tight_layout()
plt.show()

print("\nSummary of findings:")
print("The tips dataset contains restaurant bill and tip data.")