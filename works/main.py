import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir = "tests", pattern="test_sorting*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)
    