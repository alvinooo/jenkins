import tutorial
import unittest

class TestTutorial(unittest.TestCase):
  def test_hello(self):
    self.assertEquals(tutorial.hello(), "Hello")
