import unittest
import pytest
# import ipdb
# import json
from app import metrics


# python -m pytest tests/test_health_check.py
@pytest.fixture
def test_health_check(client):
    response = client.get('/status')
    assert response.json == [
        {'user': 'admin'},
        {'result': 'OKddsds - Healthy'}
    ]

class HealthStatusCase(unittest.TestCase):
    
    # python -m unittest tests/test_health_check.py
    def test_metrics(self):
        response = metrics()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
        