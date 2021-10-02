""" This program requests repository and commit information from GitHub using
the requests & json modules and the public GitHub API. """

# Modules
import requests
import json


def gather_repos(github_id):
    """ This function takes a username as input and returns a list of
    repositories found in Github for that user ID. """

    repos_list = []

    url = 'https://api.github.com/users/' + github_id + '/repos'
    response = requests.get(url)

    repos = json.loads(response.text)

    for repo in repos:
        if repo['name']:
            repos_list.append(repo['name'])
        elif repo['full_name']:
            repos_list.append(repo['full_name'])
        else:
            repos_list.append(repo['id'])

    return repos_list

def gather_commits(github_id, repo_name):
    """ This function takes a username & repo name as input and returns
    a tuple with the repo and number of commits. """

    url = 'https://api.github.com/repos/' + github_id + '/' + repo_name + '/commits'
    reponse = requests.get(url)

    commits = json.loads(reponse.text)

    commit_count = 0

    for commit in commits:
        commit_count += 1

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
