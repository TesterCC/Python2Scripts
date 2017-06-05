import unittest

# http://coding.imooc.com/lesson/53.html#mid=1728  3-7

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "Test SetUp"

    def test_something(self):
        print "Test Something"
        self.assertEqual(True, False)

    def test_anything(self):
        print "Test Anything"
        self.assertEqual(True, True)

    def tearDown(self):
        print "Test TearDown"

if __name__ == '__main__':
    unittest.main()
