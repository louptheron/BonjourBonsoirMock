from __future__ import absolute_import
import unittest
import mock

from app.main import Service


class TestBonjourBonsoir(unittest.TestCase):

    @mock.patch('app.main.Clock')
    def test_should_say_bonsoir(self, mock_clock):
        # Given
        mock_clock.get_hour.return_value = 14
        service = Service(mock_clock)
        name = ''
        # When

        # Then
        self.assertEqual('Bonsoir ', service.bonjour_bonsoir(name))

    @mock.patch('app.main.Clock')
    def test_should_say_bonsoir_Jerome(self, mock_clock):
        # Given
        mock_clock.get_hour.return_value = 14
        service = Service(mock_clock)
        name = 'Jerome'
        # When

        # Then
        self.assertEqual('Bonsoir Jerome', service.bonjour_bonsoir(name))

    @mock.patch('app.main.Clock')
    def test_should_say_bonjour_Jerome_if_before_noon(self, mock_clock):
        # Given
        mock_clock.get_hour.return_value = 11
        service = Service(mock_clock)
        name = 'Loulou'

        # When

        # Then
        self.assertEqual('Bonjour Loulou', service.bonjour_bonsoir(name))