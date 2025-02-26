import unittest
from unittest.mock import patch,MagicMock
from instance import post,retrieve,delete

class TestAPI(unittest.TestCase):
    @patch('instance.Mastodon')
    def test_post(self,MockMastodon):
        mock_instance=MockMastodon.return_value
        mock_instance.status_post.return_value={"id":114068569195091818,"content":"hello world"}

        result=post("hello world")
        self.assertEqual(result,114068569195091818)

    @patch('instance.Mastodon')
    def test_retrieve(self,MockMastodon):
        mock_instance=MockMastodon.return_value
        mock_instance.status.return_value={"id":1,"content":"nice to meet you"}

        result=retrieve(1)
        self.assertEqual(result,"nice to meet you")
 
    @patch('instance.Mastodon')
    def test_delete(self,MockMastodon):
        mock_instance=MockMastodon.return_value
        mock_instance.status_delete.return_value={"id":123,"content":"hello"}

        result=delete(123)
        self.assertEqual(result,"hello")

    if __name__ == "__main__":
        unittest.main()