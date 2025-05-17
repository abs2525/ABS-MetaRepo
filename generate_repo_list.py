"""
README Generator for ABS-MetaRepo
---------------------------------
Fetches real public repositories from specified GitHub accounts
and outputs a markdown list for README.md.

Author: abs2525
"""

import requests

# GitHub usernames and types (user or org)
accounts = [
    ("users", "abs2525", "👨‍💻 Personal Projects"),
    ("orgs", "zebrappsai", "🏢 Zebrapps.ai"),
    ("users", "avimentorysai", "🚀 Mentorys.ai")
]

# Output file
output_file = "generated_README.md"

# GitHub API base
base_url = "https://api.github.com"
print("Writing to generated_README.md in current folder...")
# Create the markdown content
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 🚀 ABS-MetaRepo\n\n")
    f.write("This repository lists my GitHub projects across personal learning, startups, and current ventures.\n\n")

    for acc_type, name, label in accounts:
        f.write(f"## {label} (`{name}`)\n")
        url = f"{base_url}/{acc_type}/{name}/repos?per_page=100"

        try:
            res = requests.get(url)
            res.raise_for_status()
            repos = res.json()

            if not repos:
                f.write("*No public repositories found.*\n")
            else:
                for repo in repos:
                    repo_name = repo["name"]
                    repo_url = repo["html_url"]
                    description = repo["description"] or "No description."
                    f.write(f"- [{repo_name}]({repo_url}) – {description}\n")
        except Exception as e:
            f.write(f"*Error fetching repos for `{name}`: {e}*\n")

        f.write("\n")

print(f"✅ Repo list saved to: {output_file}")
