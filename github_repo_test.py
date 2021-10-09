import unittest
from unittest.mock import MagicMock,patch
from hw04_zhianghu import *
class Testget_repositories(unittest.TestCase):
    @patch("hw04_zhianghu.get_repositories")
    def testget_repositories(self,Mocktest):
        list1 = ['Repo: csp Commits number: 2', 
                 'Repo: hellogitworld Commits number: 30',
                 'Repo: helloworld Commits number: 6',
                 'Repo: Mocks Commits number: 10', 
                 'Repo: Project1 Commits number: 2', 
                 'Repo: richkempinski.github.io Commits number: 9',
                 'Repo: threads-of-life Commits number: 1',
                 'Repo: try_nbdev Commits number: 2',
                 'Repo: try_nbdev2 Commits number: 5']
        self.assertEqual('Repo: csp Commits number: 2', list1[0])

if __name__ == '__main__':
    print('tests begin')
    unittest.main(exit=False, verbosity=2)

