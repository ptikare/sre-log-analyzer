# 📊 SRE Log Analyzer – Python Tool for Log Monitoring & Error Detection
-A lightweight log analysis tool that helps identify errors, warnings, and patterns in system logs — inspired by real-world SRE debugging workflows.


## 🚀 Features
- Parses log files efficiently
- Counts ERROR, WARNING, and INFO logs
- Identifies most frequent error messages
- Supports CLI input for dynamic log file analysis
- Displays Top N error messages for better insights


## 🔄 Recent Enhancements
- Added CLI-based input handling for flexible log analysis
- Implemented Top N error detection using collections.Counter
- Improved output formatting for better readability


## 🎯 Why This Project
In real-world systems, logs grow rapidly and manually scanning them during incidents is inefficient.  
This project demonstrates how automated log analysis can help in faster debugging and better observability.


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


## 5. Screenshot section
<img width="877" height="305" alt="CLI_output" src="https://github.com/user-attachments/assets/ecdf6a07-2ff9-4c7c-88a3-b095e17c7a1a" />

Example output using CLI-based log analyzer with Top N error detection


## ▶️ How to Run

1. Clone the repository  
```bash
git clone https://github.com/ptikare/sre-log-analyzer.git
cd sre-log-analyzer
```
2. Run the script using:
```bash
python src/cli_analyzer.py logs/sample.log
```


## 📁 Project Structure

sre-log-analyzer/
│── src/                         # Source code
│   ├── log_analyzer.py          # Basic log analyzer
│   └── cli_analyzer.py          # CLI-based analyzer with Top N errors
│
│── logs/                        # Sample log files
│   └── sample.log
│
│── README.md                    # Project documentation


## 📌 Use Case
This tool can be used by developers and SREs to quickly analyze logs during debugging, reducing manual effort and improving incident response time.


## 💡 Future Improvements
- Add regex-based log parsing for structured analysis
- Implement real-time log monitoring (tail -f style)
- Detect error spikes over time
- Integrate alerting (email/Slack notifications)
  
