# Flow 29
# Task 3
# I did not manage to do 3.5 plotting properly so you get a wrong png for that

import pandas as pd
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv'
drugs = pd.read_csv(url)
drugs['Date'] = pd.to_datetime(drugs['Date'])

# Task 3.1
drugs_2014year=(drugs['Date'] >= '2014-01-01') & (drugs['Date'] <= '2014-12-31')
drugs2014=drugs.loc[drugs_2014year]
drugs2014_sliced = drugs2014[['Store', 'Sales']]
drugs2014_sliced.set_index('Store', inplace=True)
print(drugs2014_sliced.groupby('Store')['Sales'].sum())

# Task 3.2
lowest_std = drugs.groupby('Store')['Sales'].std().min()
lowest_stdstore = drugs.loc[drugs.groupby('Store')['Sales'].std().idxmin()]
print(lowest_std)
print(lowest_stdstore)

# Task 3.3
drugs33 = pd.read_csv(url)
drugs33['Date'] = pd.to_datetime(drugs33['Date'])
drugs33['Month'] = drugs33['Date'].dt.to_period('M')
monthly_sales_trend = drugs33[['Store', 'Month', 'Sales']]
monthly_sales_trend = monthly_sales_trend.groupby(['Store', 'Month'])['Sales'].sum()
print(monthly_sales_trend)


# Task 3.4
avg_sales = drugs.groupby('DayOfWeek')['Sales'].mean()
plt.figure()
avg_sales.plot()
plt.savefig("34.png")

# Task 3.5
sum_sales = avg_sales = drugs.groupby('Store')['Sales'].sum()
sum_sales = sum_sales.to_frame()
sum_sales.reset_index(inplace=True)
largest = sum_sales['Sales'].nlargest(n=5)
print(largest)
drugs.set_index('Store', inplace=True)
top5drugs = drugs[drugs['Sales'].isin(largest)]
plt.figure
top5drugs.groupby('Date')['Sales'].plot(legend=True)
plt.savefig("35.png")
# I did not manage to fix this one and give the correct graph. Had trouble making python identify the 5 stores when plotting