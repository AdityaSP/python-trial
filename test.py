import unittest
class TestMy(unittest.TestCase):
  def test_add(self):
    assert 1==1
if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
