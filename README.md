# Python Log Analyzer

A Python-based cybersecurity project that analyzes authentication log entries and detects suspicious failed SSH login attempts.

## Purpose
This project was built to understand how security analysts can examine authentication logs to identify repeated failed login attempts, suspicious IP addresses, and targeted usernames.

## Features
- Parses auth-style log entries using Python regex.
- Detects failed SSH login attempts.
- Counts failed attempts by IP address.
- Counts failed attempts by username.
- Flags suspicious IPs based on a threshold.
- Displays matched log entries for review.

## How It Works
The script reads a sample log file and uses a regular expression to extract:
- Timestamp
- Username
- Source IP address
- Port number

It then:
- Counts how many failed attempts came from each IP.
- Counts how many times each username was targeted.
- Flags IP addresses with failed attempts greater than or equal to a defined threshold.

## Example Use
This project simulates a simple security monitoring task similar to checking `/var/log/auth.log` on Linux systems for failed SSH login activity.

## Sample Output
Add your output screenshot here after running the script.

## Ethical Note
This project is for educational purposes only. It uses sample log data and does not interact with live systems.

## Concepts Practiced
- Python regex
- Log parsing
- SSH failed login analysis
- Suspicious IP detection
- Counting and aggregation with dictionaries and Counter

## Future Improvements
- Export results to CSV
- Detect accepted logins separately
- Add timestamp-based attack windows
- Build a GUI version
- Support multiple log formats

## Author
Jay Prakash  
GitHub: [jayprakash-tech](https://github.com/jayprakash-tech)
