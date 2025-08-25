import csv
import pandas as pd
import matplotlib.pyplot as plt

data = [
    ['Date', 'Product', 'Quantity Sold', 'Revenue ($)'] ,
    ['2023-05-08','Iphone 12', 3, 250],
    ['2023-06-05','Iphone 11', 70, 1000],
    ['2023-03-12','Iphone X', 12, 509],
    ['2023-10-25','Iphone 16', 34 ,687]
]

with open('sales_data.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

df = pd.read_csv('sales_data.csv')
total_revenue = df['Revenue ($)'].sum()
best_selling_product = df.groupby('Product')['Quantity Sold'].sum().idxmax()
highest_sales_day = df.loc[df['Quantity Sold'].idxmax(), 'Date']

summary = (
    f"Total revenue : ${total_revenue} \n"
    f"The best selling product : {best_selling_product} \n"
    f"The highest sales day : {highest_sales_day} \n "
)

plt.plot(df['Date'], df['Quantity Sold'], marker = 'o')
plt.title('Sales trend over time')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()


with open('sales_summary.txt', 'w')  as file:
    file.write(summary)

print(summary)


