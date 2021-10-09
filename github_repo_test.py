import unittest

from githubrepo import getGitHubRepos, getGitHubRepoCommits

class TestGitHub(unittest.TestCase):

    #Test  1
    def testGitHubRepos1(self): 
        self.assertEqual(getGitHubRepos('richkempinski'),['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2'])

    #Test  2
    def testGitHubRepos2(self): 
        self.assertEqual(getGitHubRepos('richkpinski'),'User ID was not found')
    
    #Test  3
    def testGitHubRepoCommits1(self): 
        self.assertEqual(getGitHubRepoCommits('richkempinski', 'hellogitworld'), 30)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

