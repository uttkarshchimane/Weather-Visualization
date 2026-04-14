import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature(df):
    plt.figure()
    sns.lineplot(x='date', y='temperature', data=df)
    plt.title("Temperature Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("temp_plot.png")
    plt.close()

def plot_humidity(df):
    plt.figure()
    sns.barplot(x=df['date'].dt.strftime('%Y-%m-%d'), y=df['humidity'])
    plt.title("Humidity Levels")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("humidity_plot.png")
    plt.close()