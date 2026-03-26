import sys
from collections import Counter

def analyze_logs(file_path, top_n=3):
    error_count = 0
    warning_count = 0
    info_count = 0
    error_messages = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                    error_messages.append(line.strip().split("ERROR")[-1].strip())
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1

        error_counter = Counter(error_messages)

        print("\n--------- Log Summary ---------")
        print(f"INFO logs    : {info_count}")
        print(f"WARNING logs : {warning_count}")
        print(f"ERROR logs   : {error_count}")

        print("\n------ Top Error Messages ------")
        for error, count in error_counter.most_common(top_n):
            print(f"{error} -> {count} time(s)")

    except FileNotFoundError:
        print("Error: Log file not found.")

# CLI usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file> [top_n]")
    else:
        file_path = sys.argv[1]
        top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        analyze_logs(file_path, top_n)
