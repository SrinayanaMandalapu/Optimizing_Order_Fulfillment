import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('customer_order_details.csv')

# Explore the dataset
print(data.head())  # Display the first few rows of the dataset
print(data.info())  # Get information about the dataset

# Analyze order status
order_status_counts = data['Output'].value_counts()
plt.figure(figsize=(6, 4))
sns.countplot(x='Output', data=data)
plt.xlabel('Order Status')
plt.ylabel('Count')
plt.title('Distribution of Order Status')
plt.show()

# Analyze feedback
feedback_counts = data['Feedback'].value_counts()
plt.figure(figsize=(6, 4))
sns.countplot(x='Feedback', data=data)
plt.xlabel('Feedback')
plt.ylabel('Count')
plt.title('Distribution of Feedback')
plt.show()

# Analyze order status by demographic variables
plt.figure(figsize=(10, 6))
sns.countplot(x='Occupation', hue='Output', data=data)
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.title('Order Status by Occupation')
plt.xticks(rotation=45)
plt.legend(title='Order Status')
plt.show()

# Analyze order status by location
plt.figure(figsize=(10, 6))
sns.scatterplot(x='longitude', y='latitude', hue='Output', data=data)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Order Status by Location')
plt.legend(title='Order Status')
plt.show()