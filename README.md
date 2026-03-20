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
INFO Server started
WARNING Disk space low
ERROR Database connection failed
INFO Request processed
ERROR Timeout occurred


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
git clone https://github.com/ptikare/sre-log-analyzer
cd sre-log-analyzer/src
python log_analyzer.py sample.log
