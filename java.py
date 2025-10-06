import subprocess

# Step 1: Add all changes
subprocess.run(["git", "add", "."], check=True)

# Step 2: Commit the changes
commit_message = input("Enter commit message: ")
subprocess.run(["git", "commit", "-m", commit_message], check=True)

# Step 3: Push to GitHub
subprocess.run(["git", "push", "origin", "main"], check=True)

print("\n✅ Changes pushed successfully!")
