import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

try:
    iris = load_iris(as_frame = True)
    df = iris.frame 
    print("Iris dataset loaded succesfully")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

print("First 5 rows of dataset: ")
print(df.head())

print("\nMissing values per column: ")
print(df.isnull().sum())

if df.isnull().values.any():
    df= df.fillna(df.mean(numeric_only = True))
    print("\nMissing values have been filled.")
else:
    print("\nNo missing values found.")

print("\nBasic statistics: ")
print(df.describe())

grouped = df.groupby('target').mean()
print("\nMean values per species (target): ")
print(grouped)

plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Trend Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

plt.bar(grouped.index, grouped['petal length (cm)'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species (target)')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.show()

plt.hist(df['petal length (cm)'], bins=20, color='skyblue')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['target'])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

print("\nSummary of findings:")
print("The Iris dataset contains measurements of iris flowers.")
print("There are no missing values.")
print("Average petal length varies by species.")
print("Sepal length and petal length show a positive relationship in the scatter plot.")

# import requests 

# num = np.arange(1,11)
# mean_num = np.mean(num)
# print("Mean of numbers:", mean_num)

# summary_stats = {
#     'stud_chosen': ['SAndra', 'Collins', 'Steve'],
#     'position': ['Leader', 'Member', 'Member']

# }

# df = pd.DataFrame(summary_stats)
# print(df)


# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# if response.status_code == 200:
#     user_data = response.json()
#     print("User Data:")
#     print(user_data)
# else:
#     print("Failed to retrieve user data")

# numbers = [1, 3, 2, 5, 7, 4]
# plt.plot(numbers, marker='o')
# plt.title('Simple Line Graph')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()

# # data = {
# #     'Country' : ['kenya', 'Nigeria', 'Tanzania'],
# #     'Population' : [34.5, 50.7, 89.4]
# # }

# # df = pd.DataFrame(data)

# # # plt.bar(df['Country'], df['Population'])
# # # plt.plot(df['Country'], df['Population'], marker='o')
# # plt.pie(df['Population'], labels=df['Country'], autopct='%1.1f%%')
# # plt.title("Population of countries")
# # plt.xlabel("Country")
# # plt.ylabel("Population in millions")
# # plt.grid(True)
# # plt.show()

# # activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
# # hours = [8, 2, 8, 6]

# # plt.pie(hours, labels=activities, autopct='%1.1f%%')
# # plt.title("Daily Activities")
# # plt.show()



# # import pandas as pd
# # data = {
# #     'Name' : ['Sandra', 'Collins', 'Steve'],
# #     'Age' : [21, 19, 23],
# #     'Score' : [90,85, 100]

# # }
# # df = pd.DataFrame(data)
# # df['passed'] = df['Score'] >50
# # print(f"Students who have passed , {df['passed']}")


# # import numpy as np

# # num = np.arange(10, 51)

# # max_value = np.max(num)
# # min_value = np.min(num)

# # # Multiply all elements by 3
# # multiplied = num * 3

# # print("Maximum value:", max_value)
# # print("Minimum value:", min_value)
# # print("Multiplied by 3:", multiplied)

# # max_value = max(num)
# # min_value= min(num)


# # multiplied = [x * 3 for x in num]

# # print(num)
# # print(max_value)
# # print(min_value)
# # print(multiplied)


