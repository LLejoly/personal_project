#!/usr/bin/env python3

"""Tests for Basic Functions"""
import sys
import json
import unittest
import requests

import responseMessage


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.domain = "http://localhost:5000"
        self.token = "5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92"

    def methods_not_implemented(self, request, methods):
        url = self.domain + "/" + request + "/" + self.token
        for _, method in enumerate(methods):
            if method == 'POST':
                r = requests.post(url)
                self.assertEqual(r.status_code, 405)
            elif method == 'GET':
                r = requests.get(url)
                self.assertEqual(r.status_code, 405)
            elif method == 'PUT':
                r = requests.put(url)
                self.assertEqual(r.status_code, 405)
            elif method == 'DELETE':
                r = requests.delete(url)
                self.assertEqual(r.status_code, 405)

    def check_result_with_bad_token(self, request):
        url = self.domain + "/" + request + "/" + self.token + "u"
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)

    def test_check_token_methods(self):
        self.methods_not_implemented("check_token", ['PUT', 'POST', 'DELETE'])

    ## test types requests
    def test_check_token(self):
        url = self.domain + "/check_token/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_check_token_bad(self):
        self.check_result_with_bad_token("check_token")

    def test_check_token_details(self):
        url = self.domain + "/check_token/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_TOKEN)

    def test_check_token_status(self):
        url = self.domain + "/check_token/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['status'], 400)

    def test_types(self):
        url = self.domain + "/types/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_types_404(self):
        url = self.domain + "/type/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_types_empty_token(self):
        url = self.domain + "/types/"
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_types_bad_token(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)

    def test_types_bad_token_details(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_TOKEN)

    def test_types_bad_token_status(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['status'], 400)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
