import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
def load_data(filename):
    df = pd.read_csv(filename)
    return df

# Basic Data Exploration
def explore_data(df):
    print(df.describe())  # Get summary statistics
    print(df.isnull().sum())  # Check for missing values
    print(df['Weather'].value_counts())  # Check unique weather conditions

# Visualization: Temperature Distribution
def plot_temperature_distribution(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Temperature (°C)'], bins=10, kde=True, color='skyblue')
    plt.title('Temperature Distribution Across Cities')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.show()

# Visualization: Average Temperature by City
def plot_avg_temp_by_city(df):
    avg_temp_by_city = df.groupby('City')['Temperature (°C)'].mean()
    plt.figure(figsize=(10, 6))
    avg_temp_by_city.plot(kind='bar', color='coral')
    plt.title('Average Temperature by City')
    plt.xlabel('City')
    plt.ylabel('Average Temperature (°C)')
    plt.xticks(rotation=45)
    plt.show()

# Visualization: Weather Condition Distribution
def plot_weather_condition_distribution(df):
    weather_counts = df['Weather'].value_counts()
    plt.figure(figsize=(7, 7))
    weather_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
    plt.title('Weather Condition Distribution')
    plt.ylabel('')  # Remove y-axis label for clarity
    plt.show()

