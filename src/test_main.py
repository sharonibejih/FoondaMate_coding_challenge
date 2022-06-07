from main import outcome
import unittest

class TestSentClassification(unittest.TestCase):
    def test_outcome(self):
        self.assertEqual(outcome("Can I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(outcome("I will share your email"),"<tag> Student has shared")
        self.assertEqual(outcome("I shall share your email"),"<tag> Student has shared")
        self.assertEqual(outcome("I've shared your email"),"<tag> Student has shared")
        self.assertEqual(outcome("May I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(outcome("Should I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(outcome("I already shared the email"),"<tag> Student has shared")
        self.assertEqual(outcome("I've just shared your email"),"<tag> Student has shared")
        self.assertEqual(outcome("Am I allowed to share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(outcome("Am I able to share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(outcome("I am able to share your email"),"<tag> Student has shared")
        self.assertEqual(outcome("Will you help my friends if I share your email with them?"),"<tag> Student wants to know if can share")

if __name__=="__main__":
    unittest.main()