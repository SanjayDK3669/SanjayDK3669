import requests, re, os
from github import Github

# --- CONFIGURATION ---
USERNAME = "SanjayDK3669"
LEETCODE_USERNAME = "sanjay_dk"
HACKERRANK_USERNAME = "dksanjay391"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

# --- FETCH LEETCODE PROBLEMS ---
leetcode_api = f"https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}"
try:
    leetcode_data = requests.get(leetcode_api, headers=headers).json()
    leetcode_solved = leetcode_data.get("totalSolved", 0)
except:
    leetcode_solved = 0

# --- FETCH HACKERRANK BADGES ---
hackerrank_api = f"https://www.hackerrank.com/rest/hackers/{HACKERRANK_USERNAME}/badges"

try:
    res = requests.get(hackerrank_api, headers=headers)
    hackerrank_data = res.json()   # may fail if HTML returned
    hackerrank_solved = len(hackerrank_data.get("models", []))
except Exception:
    hackerrank_solved = 0   # fallback

# --- OPEN README ---
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# --- UPDATE COUNTERS ---
new_readme = re.sub(r"LeetCode Solved-\d+", f"LeetCode Solved-{leetcode_solved}", readme)
new_readme = re.sub(r"HackerRank Solved-\d+", f"HackerRank Solved-{hackerrank_solved}", new_readme)

# --- SAVE CHANGES ---
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("Updated README successfully!")
