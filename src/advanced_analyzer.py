import re
from collections import Counter, defaultdict
from datetime import datetime

# Regex pattern (adjust based on your log format)
LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)"

def parse_logs(file_path):
    info_count = 0
    warning_count = 0
    error_count = 0

    error_messages = []
    error_timestamps = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.match(LOG_PATTERN, line)
                if match:
                    timestamp_str, level, message = match.groups()
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

                    if level == "INFO":
                        info_count += 1
                    elif level == "WARNING":
                        warning_count += 1
                    elif level == "ERROR":
                        error_count += 1
                        error_messages.append(message.strip())
                        error_timestamps.append(timestamp)

        return info_count, warning_count, error_count, error_messages, error_timestamps

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None


def detect_error_spikes(error_timestamps, threshold=2, window_minutes=5):
    spike_detected = False
    error_timestamps.sort()

    for i in range(len(error_timestamps)):
        count = 1
        for j in range(i + 1, len(error_timestamps)):
            diff = (error_timestamps[j] - error_timestamps[i]).total_seconds() / 60
            if diff <= window_minutes:
                count += 1
            else:
                break

        if count >= threshold:
            print(f"\n⚠️ High error rate detected: {count} errors within {window_minutes} minutes")
            spike_detected = True
            break

    if not spike_detected:
        print("\n✅ No significant error spikes detected")


def analyze(file_path, top_n=3):
    result = parse_logs(file_path)
    if not result:
        return

    info_count, warning_count, error_count, error_messages, error_timestamps = result

    print(f"\nAnalyzing file: {file_path}")

    print("\n--------- Log Summary ---------")
    print(f"INFO logs    : {info_count}")
    print(f"WARNING logs : {warning_count}")
    print(f"ERROR logs   : {error_count}")

    # Top errors
    error_counter = Counter(error_messages)

    print(f"\n------ Top {top_n} Error Messages ------")
    for error, count in error_counter.most_common(top_n):
        print(f"{error} -> {count} time(s)")

    # Spike detection
    detect_error_spikes(error_timestamps)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python advanced_analyzer.py <log_file> [top_n]")
    else:
        file_path = sys.argv[1]
        top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        analyze(file_path, top_n)
