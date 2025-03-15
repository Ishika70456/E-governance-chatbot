import unittest
import json
from chatblot import app

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_tax_policy(self):
        response = self.app.post("/chat", json={"query": "Tell me about tax policy"})
        data = json.loads(response.data)
        self.assertIn("taxation", data["response"].lower())

if __name__ == "__main__":
    unittest.main()
