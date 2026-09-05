import os
import subprocess
from datetime import datetime
import sys 

# Path to your local repository directory
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def run_git_command(command):
    result = subprocess.run(command, cwd=REPO_DIR, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(command)}:\n{result.stderr}", file=sys.stderr)
    else:
        print(result.stdout)

def make_daily_commit():
    file_path = os.path.join(REPO_DIR, "activity.txt")
    
    # Append current timestamp to the file
    with open(file_path, "a") as f:
        f.write(f"Updated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Execute Git commands
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", f"Daily update: {datetime.now().strftime('%Y-%m-%d')}"])
    run_git_command(["git", "push", "origin", "main"])

if __name__ == "__main__":
    make_daily_commit()
