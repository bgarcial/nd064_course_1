import unittest
from app import health_check, metrics

class HealthStatusCase(unittest.TestCase):

    """ def test_health_check(self):
        result = {
            'status':'success',
            'code': 0,
            'data': {
                'UserCount': 140,
                'UserCountActive': 235555
            }
        }
        self.assertTrue(result) """
    
    def test_metrics(self):
        response = metrics()
        self.assertEqual(response.status, 200)