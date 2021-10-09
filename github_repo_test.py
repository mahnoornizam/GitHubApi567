import json
import unittest
from unittest.mock import Mock, patch

from gituhbrepo import getGitHubRepos, getGitHubRepoCommits

class TestGitHub(unittest.TestCase):

    #Test  1
    @patch('requests.get')
    def test_mock_getGitHubRepos1(self,mock_get):
        '''mocking getGitHubResponse'''
        mock_get.return_value.json.return_value = [
            {"name": "csp"},
            {"name": "hellogitworld"},
            {"name": "helloworld"},
            {"name": "Mocks"},
            {"name": "Project1"},
            {"name": "richkempinski.github.io"},
            {"name": "threads-of-life"},
            {"name": "try_nbdev"},
            {"name": "try_nbdev2"}
        ]
        
        expected_names = ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2']
        
        result = getGitHubRepos('richkempinski')
        
        self.assertEqual(result, expected_names)
        
    #Test  2
    @patch('requests.get')
    def test_mock_getGitHubRepos2(self, mock_get): 
        '''mocking getGitHubResponse'''
        mock_get.return_value.json.return_value = {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user"
        }
        
        expected_names = 'User ID was not found'
        
        result = getGitHubRepos('rihkempinski')
        self.assertEqual(result, expected_names)
    
    #Test  3
    @patch('requests.get')
    def test_mock_GitHubRepoCommits1(self, mock_get): 
        '''mocking GitHubRepoCommits'''
        mock_get.return_value.json.return_value = [
            {"commit": 1},
            {"commit": 2},
            {"commit": 3},
            {"commit": 4},
            {"commit": 5},
            {"commit": 6},
            {"commit": 7},
            {"commit": 8},
            {"commit": 9},
            {"commit": 10},
            {"commit": 11},
            {"commit": 12},
            {"commit": 13},
            {"commit": 14},
            {"commit": 15},
            {"commit": 16},
            {"commit": 17},
            {"commit": 18},
            {"commit": 19},
            {"commit": 20},
            {"commit": 21},
            {"commit": 22},
            {"commit": 23},
            {"commit": 24},
            {"commit": 25},
            {"commit": 26},
            {"commit": 27},
            {"commit": 28},
            {"commit": 29},
            {"commit": 30},
        ]
        expected_commits = 30
        
        result = getGitHubRepoCommits('richkempinski', 'hellogitworld')
        self.assertEqual(result, expected_commits)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

