import app
import unittest
from app.models import Sources


class SourceTest(unittest.TestCase):
    """Test source class"""

    def setUp(self):
        self.new_article = Sources(
            1234, 'Karls Aden', 'mydescription', 'url', 'mycategory', 'mycountry', 'mylanguage')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,1234)
        self.assertEquals(self.new_article.name,'Karls Aden')
        self.assertEquals(self.new_article.description,'mydescription')
        self.assertEquals(self.new_article.url,'url')
        self.assertEquals(self.new_article.category,'mycategory')
        self.assertEquals(self.new_article.country,'mycountry')
        self.assertEquals(self.new_article.language,'mylanguage')