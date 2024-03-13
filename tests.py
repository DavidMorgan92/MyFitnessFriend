from django.test import TestCase
from unittest.mock import patch, MagicMock
from url_tools import reverse_with_params


@patch('url_tools.reverse')
class UrlToolsTests(TestCase):
    def test_reverse_with_params_appends_url_params(self, mock_reverse: MagicMock):
        mock_reverse.return_value = 'test_url'
        result = reverse_with_params('route_name', get={'param': 'value'})
        mock_reverse.assert_called_once_with('route_name')
        self.assertEqual('test_url?param=value', result)

    def test_reverse_with_params_does_not_append_url_params(self, mock_reverse: MagicMock):
        mock_reverse.return_value = 'test_url'
        result = reverse_with_params('route_name')
        mock_reverse.assert_called_once_with('route_name')
        self.assertEqual('test_url', result)

    def test_reverse_with_params_passes_other_kwargs(self, mock_reverse: MagicMock):
        mock_reverse.return_value = 'test_url'
        result = reverse_with_params('route_name', other_kwarg='test_kwarg', get={'param': 'value'})
        mock_reverse.assert_called_once_with('route_name', other_kwarg='test_kwarg')
        self.assertEqual('test_url?param=value', result)

    def test_reverse_with_params_appends_multiple_url_params(self, mock_reverse: MagicMock):
        mock_reverse.return_value = 'test_url'
        result = reverse_with_params('route_name', get={'param1': 'value1', 'param2': 'value2', 'param3': 'value3'})
        mock_reverse.assert_called_once_with('route_name')
        self.assertEqual('test_url?param1=value1&param2=value2&param3=value3', result)
