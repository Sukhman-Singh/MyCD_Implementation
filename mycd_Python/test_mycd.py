import unittest
from mycd import getOutputString


class TestSum(unittest.TestCase):

    def test_provided_tests(self):
        self.assertEqual(getOutputString("/", "abc"), "/abc", "Expected Output: /abc")
        self.assertEqual(getOutputString("/abc/def", "ghi"), "/abc/def/ghi", "Expected Output: /abc/def/ghi")
        self.assertEqual(getOutputString("/abc/def", ".."), "/abc", "Expected Output: /abc")
        self.assertEqual(getOutputString("/abc/def", "/abc"), "/abc", "Expected Output: /abc")
        self.assertEqual(getOutputString("/abc/def", "/abc/klm"), "/abc/klm", "Expected Output: /abc/klm")
        self.assertEqual(getOutputString("/abc/def", "../.."), "/", "Expected Output: /")
        self.assertEqual(getOutputString("/abc/def", "../../.."), "/", "Expected Output: /")
        self.assertEqual(getOutputString("/abc/def", "."), "/abc/def", "Expected Output: /abc/def")
        self.assertEqual(getOutputString("/abc/def", "..klm"), "..klm: No such file or directory",
                         "Expected Output: ..klm: No such file or directory")
        self.assertEqual(getOutputString("/abc/def", "//////"), "/", "Expected Output: /")
        self.assertEqual(getOutputString("/abc/def", "......"), "......: No such file or directory",
                         "Expected Output: ......: No such file or directory")
        self.assertEqual(getOutputString("/abc/def", "../gh///../klm/."), "/abc/klm", "Expected Output: /abc/klm")

    def test_nonalphanum_current_directory_input(self):
        self.assertEqual(getOutputString("/&&&", "def"),
                         "&&&: No such file or directory (current directory input)",
                         "Expected Output: &&&: No such file or directory (current directory input)")
        self.assertEqual(getOutputString("/abc/&&&", "def/ghi"),
                         "&&&: No such file or directory (current directory input)",
                         "Expected Output: &&&: No such file or directory (current directory input)")
        self.assertEqual(getOutputString("/abc/&&&/ghi", "../def"),
                         "&&&: No such file or directory (current directory input)",
                         "Expected Output: &&&: No such file or directory (current directory input)")

    def test_nonalphanum_new_directory_input(self):
        self.assertEqual(getOutputString("/abc", "%"),
                         "%: No such file or directory",
                         "Expected Output: %: No such file or directory")
        self.assertEqual(getOutputString("/abc", "%$&"),
                         "%$&: No such file or directory",
                         "Expected Output: %$&: No such file or directory")
        self.assertEqual(getOutputString("/abc", "def/%$&"),
                         "%$&: No such file or directory",
                         "Expected Output: %$&: No such file or directory")
        self.assertEqual(getOutputString("/abc/def", "def/%$&/ghi"),
                         "%$&: No such file or directory",
                         "Expected Output: %$&: No such file or directory")
        self.assertEqual(getOutputString("/abc/def/ghi", "def/%$&/../ghi"),
                         "%$&: No such file or directory",
                         "Expected Output: %$&: No such file or directory")


if __name__ == '__main__':
    unittest.main()
