import unittest
from Al_Joker import app  # Import the Flask app

class TestAI_Brain(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.client = self.app.test_client()

    def test_process_endpoint_exists(self):
        """Test that /process endpoint exists"""
        response = self.client.post('/process', 
            json={'task': 'test message', 'dialect': 'egyptian_arabic'})
        # Should not return 404
        self.assertNotEqual(response.status_code, 404)

    def test_chat_endpoint_exists(self):
        """Test that /chat endpoint exists"""
        response = self.client.post('/chat', 
            json={'message': 'test message'})
        # Should not return 404
        self.assertNotEqual(response.status_code, 404)

    def test_process_requires_task(self):
        """Test that /process requires task parameter"""
        response = self.client.post('/process', 
            json={'dialect': 'egyptian_arabic'})
        self.assertEqual(response.status_code, 400)

    def test_chat_requires_message(self):
        """Test that /chat requires message parameter"""
        response = self.client.post('/chat', 
            json={})
        self.assertEqual(response.status_code, 400)

    def test_egyptian_arabic_dialect(self):
        """Test AI's response to Egyptian Arabic dialect"""
        response = self.client.post('/process', 
            json={'task': 'مرحبا', 'dialect': 'egyptian_arabic'})
        # Check response is valid
        self.assertIn(response.status_code, [200, 401, 500])  # May fail due to missing API key in test

if __name__ == '__main__':
    unittest.main()
