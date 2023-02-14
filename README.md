# Lab 3 Assignment
**No dependencies outside of the base Python library are required to run any of Python programs.**

## Part 1
In order to properly run these three programs, first open the src/lab3 files and run: 
- pt1_1_downloadlog.py
- pt1_3_counttotal.py
- pt1_3_entrieslast6months.py  

**NOTE: Must be run in that order.**

We have also included a screenshot of the script working on Canvas.

## Part 2
In order to properly run these three programs, first open the src/lab3 files and run: 
- pt2_1_logseachday.py
- pt2_2_monthrequests.py
- pt2_2_weekbyweek.py
- pt2_3_4xxerrorcodes.py
- pt2_4_3xxerrorcodes.py
- pt2_5_mostrequested.py
- pt2_6_leastrequested.py

## Modules
regex_parse.py  
Used for parsing through line in an Apache http log  
> http_parse(log_line) - Parses an Apache HTTP log line into a dictionary representation

log_reader.py  
Provides a function for reading log files and returning their lines as a list, with newline characters stripped.  
> read_log(file_arg) - Reads a log file and returns its lines as a list, with newline characters stripped.
