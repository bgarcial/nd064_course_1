#!/usr/bin/env python3

# This method will be used by the mock to replace requests.get/post/delete

def create_mock(status_code, data):
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        return MockResponse(status_code, data)

    return mocked_requests
