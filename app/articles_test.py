import unittest
from models import articles

Articles=articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('null','BBC News' 'https://www.facebook.com/bbcnews','Bill Gates on Elon Musk feud and Jeffrey Epstein meetings - BBC','The Microsoft tycoon talks to the BBC about divorce, conspiracy theories and Elon Musk.','https://www.bbc.com/news/technology-61329167','https://ichef.bbci.co.uk/news/1024/branded_news/174DC/production/_124425459_gettyimages-1236298089.jpg','2022-05-05T01:05:23Z','By James ClaytonNorth America technology reporter\r\nImage source, Getty Images\r\nIn a wide-ranging interview with the BBCs Today programme, Bill Gates says conspiracy theories about him are \"crazy\" an… [+3438 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()