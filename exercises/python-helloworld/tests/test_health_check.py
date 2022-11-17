import unittest
import ipdb
import json
from app import health_check, metrics

class HealthStatusCase(unittest.TestCase):

    def test_health_check(self):
        response = health_check()
        self.assertEqual(response, ['200 OK'])
    
    def test_metrics(self):
        response = metrics()
        self.assertEqual(response.status_code, 200)
        