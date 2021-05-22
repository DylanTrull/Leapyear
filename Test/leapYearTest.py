import unittest
import leapYear


class TestYear(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(leapYear.leapYear(4), True)

    def test_NotEqual(self):
        self.assertNotEqual(leapYear.leapYear(5), True)

    def test_testTrue(self):
        self.assertTrue(leapYear.leapYear(400))

    def test_testFalse(self):
        self.assertFalse(leapYear.leapYear(500))


if __name__ == '__main__':
    unittest.main()
