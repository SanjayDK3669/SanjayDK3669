import requests, re

# --- CONFIGURATION ---
LEETCODE_USERNAME = "sanjay_dk"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

# --- FETCH LEETCODE PROBLEMS ---
leetcode_api = f"https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}"

try:
    response = requests.get(leetcode_api, headers=headers)
    data = response.json()
    leetcode_solved = data.get("totalSolved", 0)
except Exception:
    leetcode_solved = 0

# --- OPEN README ---
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# --- UPDATE COUNTERS IN README ---
new_readme = re.sub(
    r"LeetCode Solved-\d+",
    f"LeetCode Solved-{leetcode_solved}",
    readme
)

# --- SAVE CHANGES ---
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("README updated with latest LeetCode stats.")
