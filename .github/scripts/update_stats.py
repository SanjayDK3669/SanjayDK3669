import requests
import re
import os

# ---------------------------
# CONFIGURATION
# ---------------------------
USERNAME = "SanjayDK3669"
LEETCODE_USERNAME = "sanjay_dk"
HACKERRANK_USERNAME = "dksanjay391"

# ---------------------------
# SAFE REQUEST FUNCTION
# ---------------------------
def safe_get_json(url, headers=None):
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()     # catches non-200 status
        return resp.json()          # may still fail → except below
    except Exception as e:
        print(f"[ERROR] Failed fetching: {url}")
        print("Reason:", e)
        return {}                   # return empty so script never breaks

# ---------------------------
# FETCH LEETCODE PROBLEMS
# ---------------------------
leetcode_api = f"https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}"
leetcode_data = safe_get_json(leetcode_api)
leetcode_solved = leetcode_data.get("totalSolved", 0)

print("LeetCode Solved:", leetcode_solved)

# ---------------------------
# FETCH HACKERRANK BADGES
# ---------------------------
hackerrank_api = f"https://www.hackerrank.com/rest/hackers/{HACKERRANK_USERNAME}/badges"

# Hackerrank sometimes blocks bots → use User-Agent
headers = {"User-Agent": "Mozilla/5.0"}

hackerrank_data = safe_get_json(hackerrank_api, headers=headers)

# Extract badges list safely
hacker_badges = hackerrank_data.get("models", [])
hackerrank_solved = len(hacker_badges)

print("HackerRank Badges:", hackerrank_solved)

# ---------------------------
# READ README.md
# ---------------------------
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# ---------------------------
# UPDATE LEETCODE COUNT
# ---------------------------
new_readme = re.sub(
    r"LeetCode Solved-\d+",
    f"LeetCode Solved-{leetcode_solved}",
    readme
)

# ---------------------------
# UPDATE HACKERRANK COUNT
# ---------------------------
new_readme = re.sub(
    r"HackerRank Solved-\d+",
    f"HackerRank Solved-{hackerrank_solved}",
    new_readme
)

# ---------------------------
# SAVE README.md
# ---------------------------
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("README updated successfully!")
