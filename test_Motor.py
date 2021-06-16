import unittest
from unittest import mock

from motor import motor

# todo: Write more tests for correct requirement entries
# todo: Fill test_motor_error_role
# todo: Fill test_motor_error_demand
# todo: Fill test_motor_error_reason


class TestMotor(unittest.TestCase):
    @mock.patch('motor.input', create=True)
    def test_motor_no_errors_1(self, mocked_input):
        mocked_input.side_effect = ['User', 'sell dog beds', 'earning money']
        self.assertEqual(motor(), 'As a User I want to sell dog beds because I want to earn money')

    @mock.patch('motor.input', create=True)
    def test_motor_no_errors_2(self, mocked_input):
        mocked_input.side_effect = ['dog bed manufacturer', 'selling dog beds', 'to earn money']
        self.assertEqual(motor(), 'As a dog bed manufacturer I want to sell dog beds because I want to earn money')

    @mock.patch('motor.input', create=True)
    def test_motor_error_role(self, mocked_input):
        mocked_input.side_effect = ['', '', '']
        self.assertEqual(motor(), '')

    @mock.patch('motor.input', create=True)
    def test_motor_error_demand(self, mocked_input):
        mocked_input.side_effect = ['', '', '']
        self.assertEqual(motor(), '')

    @mock.patch('motor.input', create=True)
    def test_motor_error_reason(self, mocked_input):
        mocked_input.side_effect = ['', '', '']
        self.assertEqual(motor(), '')


if __name__ == '__main__':
    unittest.main()
