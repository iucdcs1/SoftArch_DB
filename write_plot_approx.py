import numpy as np
import matplotlib.pyplot as plt

operations_write = np.array([0, 250000, 500000, 750000, 1000000])

postgresql_write_times = np.array([0, 15, 25, 40, 60])
mongodb_write_times = np.array([0, 8, 12, 18, 30])
sqlite_write_times = np.array([0, 10, 20, 30, 50])
influxdb_write_times = np.array([0, 5, 7, 12, 15])
redis_write_times = np.array([0, 2, 3, 5, 8])
plain_file_write_times = np.array([0, 20, 50, 80, 100])

def fit_polynomial(x, y, degree=2):
    coeffs = np.polyfit(x, y, degree)
    poly_func = np.poly1d(coeffs)
    return poly_func

postgresql_write_func = fit_polynomial(operations_write, postgresql_write_times)
mongodb_write_func = fit_polynomial(operations_write, mongodb_write_times)
sqlite_write_func = fit_polynomial(operations_write, sqlite_write_times)
influxdb_write_func = fit_polynomial(operations_write, influxdb_write_times)
redis_write_func = fit_polynomial(operations_write, redis_write_times)
plain_file_write_func = fit_polynomial(operations_write, plain_file_write_times)

write_x_fit = np.linspace(0, 1000000, 100)
postgresql_write_fit = postgresql_write_func(write_x_fit)
mongodb_write_fit = mongodb_write_func(write_x_fit)
sqlite_write_fit = sqlite_write_func(write_x_fit)
influxdb_write_fit = influxdb_write_func(write_x_fit)
redis_write_fit = redis_write_func(write_x_fit)
plain_file_write_fit = plain_file_write_func(write_x_fit)

plt.figure(figsize=(10, 6))

plt.plot(operations_write, postgresql_write_times, 'o', label='PostgreSQL (actual)', color='orange')
plt.plot(write_x_fit, postgresql_write_fit, '--', label='PostgreSQL (fit)', color='orange', alpha=0.5)

plt.plot(operations_write, mongodb_write_times, 'o', label='MongoDB (actual)', color='red')
plt.plot(write_x_fit, mongodb_write_fit, '--', label='MongoDB (fit)', color='red', alpha=0.5)

plt.plot(operations_write, sqlite_write_times, 'o', label='SQLite (actual)', color='pink')
plt.plot(write_x_fit, sqlite_write_fit, '--', label='SQLite (fit)', color='pink', alpha=0.5)

plt.plot(operations_write, influxdb_write_times, 'o', label='InfluxDB (actual)', color='magenta')
plt.plot(write_x_fit, influxdb_write_fit, '--', label='InfluxDB (fit)', color='magenta', alpha=0.5)

plt.plot(operations_write, redis_write_times, 'o', label='Redis (actual)', color='cyan')
plt.plot(write_x_fit, redis_write_fit, '--', label='Redis (fit)', color='cyan', alpha=0.5)

plt.plot(operations_write, plain_file_write_times, 'o', label='Plain File (actual)', color='blue')
plt.plot(write_x_fit, plain_file_write_fit, '--', label='Plain File (fit)', color='blue', alpha=0.5)

plt.title('Write Performance for Different Databases')
plt.xlabel('Number of Write Operations')
plt.ylabel('Time (sec)')
plt.legend()
plt.grid()
plt.show()

print(postgresql_write_func, mongodb_write_func, sqlite_write_func, influxdb_write_func, redis_write_func, plain_file_write_func, sep='\n')
