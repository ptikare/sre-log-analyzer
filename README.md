# 📊 SRE Log Analyzer – Python Tool for Log Monitoring & Error Detection
-A lightweight log analysis tool that helps identify errors, warnings, and patterns in system logs — inspired by real-world SRE debugging workflows.

A Python-based log analyzer designed to simulate how Site Reliability Engineers (SREs) identify errors and debug issues during production incidents.


## 🎯 Why This Project
In real-world systems, logs grow rapidly and manually scanning them during incidents is inefficient.  
This project demonstrates how automated log analysis can help in faster debugging and better observability.


## 🚀 Features
- Parses log files efficiently
- Counts ERROR, WARNING, and INFO logs
- Identifies most frequent error messages
- Easy to extend for real-world use cases


## 🛠️ Tech Stack
- Python
- File Handling
- Basic Data Structures (Dictionary, Counter)


## 📁 Project Structure
sre-log-analyzer/
│── log_analyzer.py
│── sample.log
│── README.md


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


## 5. Screenshot section
<img width="910" height="243" alt="Output Screenshot" src="https://github.com/user-attachments/assets/42f60d95-9448-4b7b-9cb3-1d9f29fac33a" />


## ▶️ How to Run

1. Clone the repository  
```bash
git clone https://github.com/ptikare/sre-log-analyzer.git
cd sre-log-analyzer
```
2. Run the script
```bash
python log_analyzer.py
```


## 💡 Future Improvements
- Add CLI support for dynamic log file input
- Implement regex-based pattern detection
- Build real-time log monitoring (tail -f style)
- Integrate alerting (email/Slack notifications)
  
