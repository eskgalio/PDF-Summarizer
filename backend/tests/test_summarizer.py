import unittest
from app.summarizer import generate_summary

class TestSummarizer(unittest.TestCase):
    def test_generate_summary(self):
        text = """Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data, without being explicitly programmed."""
        summary = generate_summary(text)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) > 0)

if __name__ == "__main__":
    unittest.main() 