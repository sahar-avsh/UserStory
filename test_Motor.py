import unittest
from unittest import mock

from motor import motor


class TestMotor(unittest.TestCase):
    @mock.patch('motor.input', create=True)
    def test_motor_no_errors_1(self, mocked_input):
        mocked_input.side_effect = ['User', 'sell dog beds', 'earning money']
        self.assertEqual(motor(), 'As a User I want to sell dog beds so that I earn money')

    @mock.patch('motor.input', create=True)
    def test_motor_no_errors_2(self, mocked_input):
        mocked_input.side_effect = ['dog bed manufacturer', 'selling dog beds', 'to earn money']
        self.assertEqual(motor(), 'As a dog bed manufacturer I want to sell dog beds so that I earn money')

    @mock.patch('motor.input', create=True)
    def test_motor_no_errors_3(self, mocked_input):
        mocked_input.side_effect = ['Consultant', 'participate in consulting projects', 'to get promoted']
        self.assertEqual(motor(), 'As a Consultant I want to participate in consulting projects so that I get promoted')


if __name__ == '__main__':
    unittest.main()
