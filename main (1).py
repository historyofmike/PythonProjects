import pandas as pd


#Load the sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')


def analyze_sales_data(data):
  #Calculate total sales
  total_sales = data['Revenue'].sum()

  #Calculate average sells on products
  average_sales = data['Revenue'].mean()

  #Calculate highest selling product
  best_selling_product = data['Product'].value_counts().idxmax()

  
  month_highest_sales = data.groupby('Month')['Revenue'].sum().idxmax()


  print("Sales Data Analysis")
  print("-------------------")
  print(f"Total Sales: ${total_sales}")
  print(f"Average Sales per Month: ${average_sales}")
  print(f"Best-Selling Product: ${best_selling_product}")
  print(f"Month with Highest Sales ${month_highest_sales}")

analyze_sales_data(sales_data)
  
