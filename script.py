import os
import subprocess
from datetime import datetime
import sys 
import time
import json

# Path to your local repository directory
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def run_git_command(command):
    result = subprocess.run(command, cwd=REPO_DIR, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(command)}:\n{result.stderr}", file=sys.stderr)
    else:
        print(result.stdout)

def make_daily_commits_3():
    activity_file = os.path.join(REPO_DIR, "activity.txt")
    counter_file = os.path.join(REPO_DIR, "count.json")
    
    # Append current timestamp to the file
    for i in range(3):
        with open(activity_file, "a") as f:
            f.write(f"Updated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            if i == 2:
                f.write("\n")
                with open(counter_file, "r") as f2:
                    data = json.load(f2)
                    data["count"] += 1
                    with open(counter_file, "w") as f:
                        json.dump(data, f, indent=4)
        
        # Execute Git commands
        run_git_command(["git", "pull"]) 
        run_git_command(["git", "add", "."])
        run_git_command(["git", "commit", "-m", f"Daily update: {datetime.now().strftime('%d-%m-%Y')}"])
        run_git_command(["git", "push", "origin", "main"])

        if i < 2:
            time.sleep(60)

if __name__ == "__main__":
    make_daily_commits_3()
