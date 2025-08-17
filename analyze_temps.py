import pandas as pd
import matplotlib.pyplot as plt


def analyze_temperatures(csv_file='temperatures.csv'):
    """
    Read temperature data from CSV and generate a bar chart showing 
    average temperature for each city.
    
    Args:
        csv_file (str): Path to the CSV file containing temperature data
        
    Returns:
        None
    """
    df = pd.read_csv(csv_file)
    
    avg_temps = df.groupby('City')['Temperature'].mean()
    
    plt.figure(figsize=(10, 6))
    avg_temps.plot(kind='bar', color=['#FF6B6B', '#4ECDC4'])
    plt.title('Average Temperature by City', fontsize=14, fontweight='bold')
    plt.xlabel('City', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('temperature_chart.png', dpi=100, bbox_inches='tight')
    plt.show()
    
    print("Average temperatures:")
    for city, temp in avg_temps.items():
        print(f"{city}: {temp:.1f}°C")
    print("\nChart saved as 'temperature_chart.png'")


if __name__ == "__main__":
    analyze_temperatures()