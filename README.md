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
-INFO Server started
-WARNING Disk space low 
-ERROR Database connection failed 
-INFO Request processed 
-ERROR Timeout occurred 


## 📈 Sample Output
=======Log Summary========== 

INFO    :  3 

WARNING :  2 

ERROR   :  5 

=======Error Details======== 

ERROR Database connection failed -> 1 time 

ERROR Timeout while calling API  -> 1 time 

ERROR Database connection failed -> 1 time 

ERROR Database connection failed -> 1 time 

ERROR Database connection failed -> 1 time 


## ▶️ How to Run
1. Clone the repository

git clone https://github.com/ptikare/sre-log-analyzer
cd sre-log-analyzer/src

2. Run the script

python log_analyzer.py sample.log
