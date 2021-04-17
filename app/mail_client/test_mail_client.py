from .mail_client import Client
import unittest


class TestClient(unittest.TestCase):
    def test_login(self):
        # Given
        client = Client()
        
        # When
        code = client._get_login_code()

        # Then
        self.assertAlmostEqual(str(code)[0], "2")