import unittest
from app.models import Articles



class ArticleTest(unittest.TestCase):
    '''
    Test class to test articles
    '''
    def setUp(self):
        self.new_article = Articles(
            1234, 'Karls Aden', 'mytitle', 'mydescription', 'url','myimage','datecreated')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,1234)
        self.assertEquals(self.new_article.author,'Karls Aden')
        self.assertEquals(self.new_article.title,'mytitle')
        self.assertEquals(self.new_article.description,'mydescription')
        self.assertEquals(self.new_article.url,'url')
        self.assertEquals(self.new_article.image,'myimage')
        self.assertEquals(self.new_article.date,'datecreated')