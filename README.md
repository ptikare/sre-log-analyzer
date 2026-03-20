# 📊 SRE Log Analyzer (Python)

A simple Python-based log analyzer that helps identify errors, warnings, and patterns in log files — similar to how SREs debug systems during incidents.

## 🚀 Features
- Parses log files efficiently
- Counts ERROR, WARNING, and INFO logs
- Identifies most frequent error messages
- Easy to extend for real-world use cases


## 🛠️ Tech Stack
- Python
- File Handling
- Basic Data Structures (Dictionary, Counter)


## 📂 Sample Log Input
2026-03-15 10:01:23 INFO Service started
2026-03-15 10:02:10 INFO User login successful
2026-03-15 10:03:11 WARNING Disk usage above 75%
2026-03-15 10:03:45 ERROR Database connection failed
2026-03-15 10:04:20 ERROR Timeout while calling API
2026-03-15 10:05:33 INFO Background job completed
2026-03-15 10:06:02 ERROR Database connection failed


## 📈 Sample Output
-------Log Summary----------

INFO logs:  3
WARNING logs:  2
ERROR logs:  5

-------Error Deatails--------

2026-03-15 10:03:45 ERROR Database connection failed 1 time
2026-03-15 10:04:20 ERROR Timeout while calling API 1 time
2026-03-15 10:06:02 ERROR Database connection failed 1 time
2026-03-15 10:06:15 ERROR Database connection failed 1 time
2026-03-15 10:06:30 ERROR Database connection failed 1 time


## ▶️ How to Run
```bash
python log_analyzer.py
