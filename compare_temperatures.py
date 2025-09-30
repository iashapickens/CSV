import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_weather(filename):
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        header_row = next(csvfile)

        date_index = header_row.index("DATE")
        tmin_index = header_row.index("TMIN")
        tmax_index = header_row.index("TMAX")
        name_index = header_row.index("NAME")

        dates, highs, lows = [], [], []
        station_name = None

        for row in csvfile:
            try:
                current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
                high = int(row[tmax_index])
                low = int(row[tmin_index])
                if not station_name:
                    station_name = row[name_index]
            except ValueError:
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows, station_name


dates_sitka, highs_sitka, lows_sitka, sitka_name = read_weather("sitka_weather_2018_simple.csv")
dates_dv, highs_dv, lows_dv, dv_name = read_weather("death_valley_2018_simple.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(dates_sitka, highs_sitka, c="red", label="High")
ax1.plot(dates_sitka, lows_sitka, c="blue", label="Low")
ax1.fill_between(dates_sitka, lows_sitka, highs_sitka, color="lightblue")
ax1.set_title(sitka_name)
ax1.set_xlabel("")
ax1.set_ylabel("Temperature (F)")
ax1.legend()

ax2.plot(dates_dv, highs_dv, c="red", label="High")
ax2.plot(dates_dv, lows_dv, c="blue", label="Low")
ax2.fill_between(dates_dv, lows_dv, highs_dv, color="lightcoral")
ax2.set_title(dv_name)
ax2.set_xlabel("Date")
ax2.set_ylabel("Temperature (F)")
ax2.legend()

fig.suptitle(f"Temperature comparison between {sitka_name} and {dv_name}", fontsize=16)

plt.tight_layout()
plt.show()
