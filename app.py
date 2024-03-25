import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend
from flask import Flask, send_file
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
import threading
from datetime import datetime, timedelta

app = Flask(__name__)
lock = threading.Lock()
request_times = []


@app.route("/")
def index():
    with lock:
        global request_times
        current_time = datetime.now()
        request_times.append(current_time)

        # Keep only the recent requests (e.g., last 10 minutes for a broader view)
        time_window_start = current_time - timedelta(minutes=10)
        request_times = [time for time in request_times if time >= time_window_start]

        # Calculate moving average over broader intervals (e.g., every 10 seconds)
        interval_seconds = 5
        times = [
            time_window_start + timedelta(seconds=i)
            for i in range(0, 600, interval_seconds)
        ]
        averages = []
        for i in range(len(times) - 1):
            time_range = [
                time for time in request_times if times[i] <= time < times[i + 1]
            ]
            averages.append(len(time_range) / interval_seconds)

        plt.figure(figsize=(10, 5))
        plt.plot(times[:-1], averages)  # Skip the last time as it's the upper bound
        plt.title("Moving Average of GET Requests (Last 10 Minutes)")
        plt.xlabel("Time")
        plt.ylabel("Requests per Second")

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
        plt.gca().xaxis.set_major_locator(mdates.MinuteLocator())
        plt.gcf().autofmt_xdate()  # Automatic rotation of date labels

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        plt.close()
        return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
