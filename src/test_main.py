from main import filter
import unittest

class TestSentClassification(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(filter("Can I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("I will share your email"),"<tag> Student has shared")
        self.assertEqual(filter("I shall share your email"),"<tag> Student has shared")
        self.assertEqual(filter("I've shared your email"),"<tag> Student has shared")
        self.assertEqual(filter("May I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("Should I share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("I already shared the email"),"<tag> Student has shared")
        self.assertEqual(filter("I've just shared your email"),"<tag> Student has shared")
        self.assertEqual(filter("Am I allowed to share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("Am I able to share your email"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("I am able to share your email"),"<tag> Student has shared")
        self.assertEqual(filter("Will you help my friends if I share your email with them?"),"<tag> Student wants to know if can share")
        self.assertEqual(filter("Will you help my friends"),
                         "'share' and 'email' are both not in given sentence: Will you help my friends.")
        self.assertEqual(filter("I would like to know your email"),
                         "'share' and 'email' are both not in given sentence: I would like to know your email.")
        

if __name__=="__main__":
    unittest.main()