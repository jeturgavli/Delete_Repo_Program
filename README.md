# Delete Repo Program

This script, `delete_repo_program.py`, allows you to delete repositories from your GitHub account using the GitHub API.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- An active GitHub account.
- Personal Access Token generated from GitHub.

## Setup

1. Clone or download this repository.
2. Navigate to the directory containing `delete_repo_program.py`.
3. Create a file named `critical_info.py` in the same directory.
4. Open `critical_info.py` and replace the placeholders `<access_token>` and `<your_username>` with your GitHub access token and username respectively.
   ```python
   # Replace <access_token> and <your_username>
   access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
   YOUR_USERNAME = "YOUR_GITHUB_USERNAME"

5. Save and close critical_info.py.

- if you dont know how to Generate Personal Access Token Click Below and Read.
## [GitHub](generate_token.md)
## Usage
1. Run the delete_repo_program.py script using Python.
```python
python delete_repo_program.py
```
2. The script will list all repositories associated with your GitHub account.
3. Enter the numbers corresponding to the repositories you want to delete, separated by spaces.
4. The script will attempt to delete the selected repositories.
# Important Note
Deleting a repository is irreversible and will permanently remove all associated data. Use with caution.
# Disclaimer
This script comes with no warranty or guarantee. Use it at your own risk. The developer is not responsible for any data loss or damages caused by the use of this script.

# Authors
- [Jetur Gavli](https://www.github.com/jeturgavli)

