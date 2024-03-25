import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend
from flask import Flask, send_file
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
import threading
from datetime import datetime

app = Flask(__name__)
lock = threading.Lock()
request_times = []


@app.route("/")
def index():
    with lock:
        current_time = datetime.now()
        request_times.append(current_time)

        plt.figure(figsize=(10, 5))
        plt.plot(request_times, list(range(1, len(request_times) + 1)))
        plt.title("GET Requests Over Time")
        plt.xlabel("Time")
        plt.ylabel("Number of GET Requests")

        # Format the x-axis to show the time more clearly
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=30))
        plt.gcf().autofmt_xdate()  # Rotation

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        plt.close()
        return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
