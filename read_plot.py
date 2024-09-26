import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Number of operations': [0, 250000, 500000, 750000, 1000000],
    'PostgreSQL': [0, 20, 30, 50, 70],
    'MongoDB': [0, 10, 20, 25, 40],
    'SQLite': [0, 5, 10, 15, 20],
    'InfluxDB': [0, 8, 12, 18, 25],
    'Redis': [0, 3, 5, 7, 10],
    'Plain File': [0, 30, 70, 100, 120],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

for db in ['PostgreSQL', 'MongoDB', 'SQLite', 'InfluxDB', 'Redis', 'Plain File']:
    plt.plot(df['Number of operations'], df[db], marker='o', label=db)

plt.title('Execution Time for Different Databases (100% Read Operations)')
plt.xlabel('Number of Operations')
plt.ylabel('Time (sec)')
plt.legend()
plt.grid()
plt.xticks(df['Number of operations'])
plt.yticks(range(0, 140, 20))

plt.savefig('database_comparison.png')
plt.show()
