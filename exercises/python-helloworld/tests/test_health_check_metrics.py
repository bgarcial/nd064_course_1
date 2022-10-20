import unittest
from unittest import mock
from unittest.mock import Mock
import json
import pytest

from mocking_http_status_codes import create_mock

# from app import health_check


class HealthStatusCase(unittest.TestCase):
    # mock is the result or output
    @mock.patch(
        'requests.get',
        side_effect=create_mock(
            200,
            {
                "response" : [
                    {
                        'user': 'admin'
                    },
                    {
                        'result': 'OK - Healthy'
                    },
                    # {
                    #     'asa': 'sad'
                    # }
                ]
            }
        )
    )
    @mock.patch('app.health_check')
    def test_health_check(self, health_check, mock):
        health_check()

    @mock.patch('requests.get',
                side_effect=create_mock(
                    200,
                    {
                        'status': 'success',
                        'code': 0,
                        'data': {
                            'UserCount': 140,
                            'UserCountActive': 2333
                        }
                    })
                )
    @mock.patch('app.metrics')
    def test_metrics(self, metrics, mock):
        metrics()


