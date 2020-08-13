import unittest
import reverse

input0 = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
output0 = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

input1 = {'a':'b'}
output1 = {'b':'a'}

input2 = {}
output2 = {}

class RevTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse.reverse(input0), output0)
        self.assertEqual(reverse.reverse(input1), output1)
        self.assertEqual(reverse.reverse(input2), output2)

if __name__ == '__main__':
    unittest.main()