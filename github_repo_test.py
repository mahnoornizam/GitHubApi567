

# Modules
import requests
import json
import unittest

# File Imports
from githubrepo import gather_repos, gather_commits, gather_github_info

class Testgithubrepo(unittest.TestCase):
    """ This class contains all of the unit tests for the GitHub Aggregator """

    def test_gather_repos(self):
        self.assertEqual(gather_repos('richkempinski'), ['threads-of-life', 'hellogitworld', 'helloworld', 'csp', 'richkempinski.io', 'Mocks', 'Project1', 'try_nbdev', 'try_nbdev2'])
        self.assertNotEqual(gather_repos('richkempinski'), ['threads-of-life', 'hellogitworld', 'helloworld', 'csp', 'richkempinski.io', 'Mocks', 'Project1', 'try_nbdev', 'try_nbdev2'])


    def test_gather_commits(self):
        self.assertEqual(gather_commits('richkempinski', 'hellogitworld'), ('hellogitworld', 11))
        self.assertNotEqual(gather_commits('richkempinski', 'hellogitworld'), ('hellogitworld', 13))


    def test_gather_github_info(self):
        self.assertEqual(gather_github_info('richkempinski'), [('threads-of-life', 9), ('hellogitworld', 6), ('helloworld', 30), ('csp', 16), ('richkempinski.io',3), ('Mocks', 11), ('Project1', 7), ('try_nbdev',9), ('try_nbdev2',11)])
        self.assertNotEqual(gather_github_info('richkempinski'), [('hellogitworld', 6), ('helloworld', 30), ('csp', 16), ('richkempinski.io',3), ('Mocks', 11), ('Project1', 7), ('try_nbdev',9), ('try_nbdev2',11)])


if __name__ == '__main__':
    print("Running Unit Tests...")
    unittest.main(exit=False,verbosity=2)
