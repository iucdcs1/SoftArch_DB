import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

operations = np.array([0, 250000, 500000, 750000, 1000000])
postgresql_times = np.array([0, 20, 30, 50, 70])
mongodb_times = np.array([0, 10, 20, 25, 40])
sqlite_times = np.array([0, 5, 10, 15, 20])
influxdb_times = np.array([0, 8, 12, 18, 25])
redis_times = np.array([0, 3, 5, 7, 10])
plain_file_times = np.array([0, 30, 70, 100, 120])

def fit_polynomial(x, y, degree=2):
    coeffs = np.polyfit(x, y, degree)
    poly_func = np.poly1d(coeffs)
    return poly_func

postgresql_func = fit_polynomial(operations, postgresql_times)
mongodb_func = fit_polynomial(operations, mongodb_times)
sqlite_func = fit_polynomial(operations, sqlite_times)
influxdb_func = fit_polynomial(operations, influxdb_times)
redis_func = fit_polynomial(operations, redis_times)
plain_file_func = fit_polynomial(operations, plain_file_times)

x_fit = np.linspace(0, 1000000, 100)
postgresql_fit = postgresql_func(x_fit)
mongodb_fit = mongodb_func(x_fit)
sqlite_fit = sqlite_func(x_fit)
influxdb_fit = influxdb_func(x_fit)
redis_fit = redis_func(x_fit)
plain_file_fit = plain_file_func(x_fit)

# Plotting the fitted functions
plt.figure(figsize=(10, 6))

plt.plot(operations, postgresql_times, 'o', label='PostgreSQL (actual)', color='orange')
plt.plot(x_fit, postgresql_fit, '--', label='PostgreSQL (fit)', color='orange', alpha=0.5)

plt.plot(operations, mongodb_times, 'o', label='MongoDB (actual)', color='red')
plt.plot(x_fit, mongodb_fit, '--', label='MongoDB (fit)', color='red', alpha=0.5)

plt.plot(operations, sqlite_times, 'o', label='SQLite (actual)', color='pink')
plt.plot(x_fit, sqlite_fit, '--', label='SQLite (fit)', color='pink', alpha=0.5)

plt.plot(operations, influxdb_times, 'o', label='InfluxDB (actual)', color='magenta')
plt.plot(x_fit, influxdb_fit, '--', label='InfluxDB (fit)', color='magenta', alpha=0.5)

plt.plot(operations, redis_times, 'o', label='Redis (actual)', color='cyan')
plt.plot(x_fit, redis_fit, '--', label='Redis (fit)', color='cyan', alpha=0.5)

plt.plot(operations, plain_file_times, 'o', label='Plain File (actual)', color='blue')
plt.plot(x_fit, plain_file_fit, '--', label='Plain File (fit)', color='blue', alpha=0.5)

plt.title('Execution Time Fit for Different Databases (100% Read Operations)')
plt.xlabel('Number of Operations')
plt.ylabel('Time (sec)')
plt.legend()
plt.grid()
plt.show()

print(postgresql_func, mongodb_func, sqlite_func, influxdb_func, redis_func, plain_file_func, sep='\n')
