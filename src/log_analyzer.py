from collections import Counter

error_messages = []
error_count = 0
warning_count = 0
info_count = 0

with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
            error_messages.append(line.strip())
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

print("-------Log Summary----------")
print("INFO logs    : ", info_count)
print("WARNING logs : ", warning_count)
print("ERROR logs   : ", error_count)

print("\n-------Error Details--------")

error_summary = Counter(error_messages)

for error, count in error_summary.items():
    print(f"{error} -> {count} time(s)")
