import requests
import critical_info as ci


url = 'https://api.github.com/user/repos'
headers = {'Authorization': f'token {ci.access_token}'}
response = requests.get(url, headers=headers)
repos = response.json()



print("Your repositories:")
for idx, repo in enumerate(repos, 1):
    print(f"{idx}. {repo['name']}")


repos_to_delete_str = input("Enter numbers of repositories to delete (separated by space): ")
repos_to_delete = [int(x) for x in repos_to_delete_str.split() if x.isdigit() and int(x) <= len(repos)]


for idx in repos_to_delete:
    repo_name = repos[idx-1]['name']
    delete_url = f'https://api.github.com/repos/{ci.YOUR_USERNAME}/{repo_name}'
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Failed to delete repository '{repo_name}'. Status code: {response.status_code}")
