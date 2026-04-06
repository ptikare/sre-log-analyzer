# 📊 SRE Log Analyzer – Python Tool for Log Monitoring & Error Detection
-A lightweight log analysis tool that helps identify errors, warnings, and patterns in system logs — inspired by real-world SRE debugging workflows.


## 🚀 Features
- Parses log files using regex for structured analysis
- Extracts timestamp, log level, and message
- Counts INFO, WARNING, and ERROR logs
- CLI support for dynamic log file input
- Displays Top N error messages using collections.Counter
- Detects error spikes based on time window (SRE use case)
- Modular project structure for scalability


## 🔄 Recent Enhancements
- Added CLI-based input handling for flexible log analysis
- Implemented Top N error detection using collections.Counter
- Introduced regex-based log parsing for structured data extraction
- Built error spike detection using time-window analysis


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

Example output showing log summary, top error messages, and error spike detection 


## ▶️ How to Run

1. Clone the repository: 
```bash
git clone https://github.com/ptikare/sre-log-analyzer.git
cd sre-log-analyzer
```
2. Run the advanced analyzer:
```bash
python src/advanced_analyzer.py logs/sample.log
```


## 📁 Project Structure

sre-log-analyzer/
│── src/                         # Source code
│   ├── log_analyzer.py          # Basic log analyzer
│   └── cli_analyzer.py          # CLI-based analyzer with Top N errors
│   └── advanced_analyzer.py     # Regex + spike detection
│
│── logs/                        # Sample log files
│   └── sample.log
│
│── README.md                    # Project documentation


## 📌 Use Case
This tool can be used by developers and SREs to quickly analyze logs during debugging, reducing manual effort and improving incident response time.


## 💡 Future Improvements
- Real-time log monitoring (tail -f style)
- Integration with alerting systems (Slack/Email)
- Visualization dashboard for log insights
- Support for multiple log formats
  
