import unittest

tw = __import__("..\\ten_min_walk.py")

print(type(tw))


class TestWalk(unittest.TestCase):

    def test_walk(self):
        w1 = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # true
        w2 = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']  # false
        w3 = ['w']  # false
        w4 = ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # false

        walks = [(w1, True), (w2, False), (w3, False), (w4, False)]

        for w in walks:
            self.assertEqual(tw.is_valid_walk(w[0]), w[1])

        for w in walks:
            self.assertEqual(tw.is_valid_walk2(w[0]), w[1])

if __name__ == '__main__':

    unittest.main()
