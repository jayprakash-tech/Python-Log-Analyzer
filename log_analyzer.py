import re
from collections import Counter, defaultdict

LOG_FILE = "sample_auth.log"
THRESHOLD = 3

pattern = re.compile(
    r"(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2})\s+\S+\s+sshd.*Failed password for (?:invalid user )?(\S+)\s+from\s+(\d+\.\d+\.\d+\.\d+)\s+port\s+(\d+)"
)

failed_attempts = []
ip_counts = Counter()
user_counts = Counter()
ip_users = defaultdict(set)

with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            timestamp, username, ip, port = match.groups()
            failed_attempts.append((timestamp, username, ip, port))
            ip_counts[ip] += 1
            user_counts[username] += 1
            ip_users[ip].add(username)

print("=" * 60)
print("LOG ANALYZER REPORT")
print("=" * 60)
print(f"Log file analyzed: {LOG_FILE}")
print(f"Total failed login attempts found: {len(failed_attempts)}")
print("-" * 60)

print("Failed login attempts by IP:")
for ip, count in ip_counts.most_common():
    print(f"- {ip}: {count} attempts")

print("-" * 60)
print("Failed login attempts by username:")
for user, count in user_counts.most_common():
    print(f"- {user}: {count} attempts")

print("-" * 60)
print(f"Suspicious IPs (threshold >= {THRESHOLD} failed attempts):")
found_suspicious = False
for ip, count in ip_counts.items():
    if count >= THRESHOLD:
        found_suspicious = True
        users = ", ".join(sorted(ip_users[ip]))
        print(f"- {ip}: {count} failed attempts | targeted users: {users}")

if not found_suspicious:
    print("No suspicious IPs found.")

print("-" * 60)
print("Sample matched log entries:")
for entry in failed_attempts[:5]:
    timestamp, username, ip, port = entry
    print(f"- {timestamp} | user={username} | ip={ip} | port={port}")

print("=" * 60)
