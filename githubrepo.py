import requests

def get_repositories(username):
    list1 = list()
    f='https://api.github.com/users/'+{username}+'/repos'
    re = requests.get(f)
    json = re.json()
    for  p  in  range ( 0 , len ( json )):
        rename = json[p]['name']
        f='https://api.github.com/repos/'+{username}+'/'+{rename}+'/commits'
        commit = requests.get(f)
        c = commit.json()
        list1.append(f"Repo: {rename} Commits number: {len(c)}")
    return list1

def main():
    username = input("Enter the username:")
    print(get_repositories(username))

if __name__=='__main__':
    main()
    return repo_name, commit_count

def gather_github_info(github_id):
    """ This function takes as input the username & returns a list of tuples
    of repo_name & commit_count for that GitHub user. """

    results_list = []

    repos_list = gather_repos(github_id)

    for repo in repos_list:
        repo_name, commit_count = gather_commits(github_id, repo)
        results_list.append((repo_name, commit_count))

    return results_list
