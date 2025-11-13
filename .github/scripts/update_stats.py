import requests, re, os
from github import Github

# --- CONFIGURATION ---
USERNAME = "SanjayDK3669"
LEETCODE_USERNAME = "sanjay_dk"
HACKERRANK_USERNAME = "dksanjay391"

# --- FETCH LEETCODE PROBLEMS ---
leetcode_api = f"https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}"
leetcode_data = requests.get(leetcode_api).json()
leetcode_solved = leetcode_data.get("totalSolved", 0)

# --- FETCH HACKERRANK BADGES ---

hackerrank_api = f"https://www.hackerrank.com/rest/hackers/{HACKERRANK_USERNAME}/badges"
hackerrank_data = requests.get(hackerrank_api).json()
hackerrank_solved = len(hackerrank_data.get("models", []))

# --- OPEN README ---
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# --- UPDATE COUNTERS ---
pattern = r"LeetCode Solved-\d+"
new_readme = re.sub(pattern, f"LeetCode Solved-{leetcode_solved}", readme)

pattern = r"HackerRank Solved-\d+"
new_readme = re.sub(pattern, f"HackerRank Solved-{hackerrank_solved}", new_readme)

# --- SAVE CHANGES ---
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
