#!/usr/bin/env python3

"""Tests for Basic Functions"""
import sys
import json
import unittest
import requests
sys.path.append('..')
import responseMessage


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.domain = "http://localhost:5000"
        self.token = "5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92"
        self.headers = {'Content-Type': 'application/json', }

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

    def test_01_check_token_methods(self):
        self.methods_not_implemented("check_token", ['PUT', 'POST', 'DELETE'])

    ## test types requests
    def test_02_check_token(self):
        url = self.domain + "/check_token/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_03_check_token_bad(self):
        self.check_result_with_bad_token("check_token")

    def test_04_check_token_details(self):
        url = self.domain + "/check_token/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_TOKEN)

    def test_05_check_token_status(self):
        url = self.domain + "/check_token/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['status'], 400)

    def test_06_types(self):
        url = self.domain + "/types/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_07_types_404(self):
        url = self.domain + "/type/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_08_types_empty_token(self):
        url = self.domain + "/types/"
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_09_types_bad_token(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)

    def test_10_types_bad_token_details(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_TOKEN)

    def test_11_types_bad_token_status(self):
        url = self.domain + "/types/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['status'], 400)

    def test_12_types_methods(self):
        self.methods_not_implemented("types", ['PUT', 'POST', 'DELETE'])

    # FREEZER
    def test_13_freezer_get(self):
        url = self.domain + "/freezers/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_14_freezer_bad_token_status(self):
        url = self.domain + "/freezers/" + self.token + "u"
        r = requests.get(url)
        content = r.json()
        self.assertEqual(content['status'], 400)

    def test_15_freezer_post(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.post(url,
                          data=json.dumps(dict(num_boxes=4,
                                               name='test')),
                          headers=headers)
        self.assertEqual(r.status_code, 200)

    def test_16_freezer_post_bad_content_type(self):
        url = self.domain + "/freezers/" + self.token
        r = requests.post(url,
                          data=json.dumps(dict(num_boxes=4,
                                               name='test')))
        self.assertEqual(r.status_code, 415)

    def test_17_freezer_post_bad_data(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.post(url,
                          data=json.dumps(dict(num_boxes="bad format",
                                               name='test')),
                          headers=headers)

        self.assertEqual(r.status_code, 400)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_FORMAT)

    def test_18_freezer_update(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.put(url,
                         data=json.dumps(dict(freezer_id=3,
                                              num_boxes="",
                                              name='updated')),
                         headers=headers)
        self.assertEqual(r.status_code, 200)

    def test_19_freezer_update_bad_content_type(self):
        url = self.domain + "/freezers/" + self.token
        r = requests.put(url,
                         data=json.dumps(dict(freezer_id=3,
                                              num_boxes="",
                                              name='updated')))
        self.assertEqual(r.status_code, 415)

    def test_20_freezer_update_bad_data(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.put(url,
                         data=json.dumps(dict(freezer_id="bad format",
                                              num_boxes="",
                                              name='updated')),
                         headers=headers)

        self.assertEqual(r.status_code, 400)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_FORMAT)

    def test_21_freezer_delete(self):
        url = self.domain + "/freezers/" + self.token
        r = requests.get(url)
        content = r.json()
        latest_freezer = max(content, key=lambda ev: ev['freezer_id'])
        latest_freezer_id = latest_freezer['freezer_id']
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.delete(url,
                            data=json.dumps(dict(freezer_id=latest_freezer_id)),
                            headers=headers)
        self.assertEqual(r.status_code, 200)

    def test_22_freezer_delete_bad_content_type(self):
        url = self.domain + "/freezers/" + self.token
        r = requests.get(url)
        content = r.json()
        latest_freezer = max(content, key=lambda ev: ev['freezer_id'])
        latest_freezer_id = latest_freezer['freezer_id']

        url = self.domain + "/freezers/" + self.token
        r = requests.delete(url,
                            data=json.dumps(dict(freezer_id=latest_freezer_id)))
        self.assertEqual(r.status_code, 415)

    def test_23_freezer_delete_bad_data(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.delete(url,
                            data=json.dumps(dict(freezer_id="bad data")),
                            headers=headers)

        self.assertEqual(r.status_code, 400)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_FORMAT)

    def test_24_freezer_delete_non_empty(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.delete(url,
                            data=json.dumps(dict(freezer_id=1)),
                            headers=headers)

        self.assertEqual(r.status_code, 400)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.DELETE_FREEZER)

    # GET NEXT FREEZER
    def test_25_get_next_freezer_id(self):
        url = self.domain + "/freezer_next_id/1/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_26_get_next_freezer_id_bad_id(self):
        url = self.domain + "/freezer_next_id/15/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)

    def test_27_get_next_freezer_id_bad_id_type(self):
        url = self.domain + "/freezer_next_id/15d/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_28_get_next_freezer_id_bad_route(self):
        url = self.domain + "/freezer_next_id/" + self.token
        r = requests.get(url)
        self.assertEqual(r.status_code, 404)

    def test_29_get_next_freezer_id_not_implemented(self):
        self.methods_not_implemented("freezer_next_id/1", ['PUT', 'POST', 'DELETE'])

    # ADD A PRODUCT
    def test_30_add_product_not_implemented_methods(self):
        self.methods_not_implemented("add_product", ['GET', 'PUT', 'DELETE'])

    def test_31_add_product_bad_content_type(self):
        url = self.domain + "/add_product/" + self.token
        r = requests.post(url,
                          data=json.dumps(dict(product_name="name",
                                               text_descr="description",
                                               freezer_id=1,
                                               type_id=1,
                                               date_in='2016-03-05',
                                               period=21,
                                               box_num=1,
                                               prod_num=15,
                                               quantity=2)))
        self.assertEqual(r.status_code, 415)

    def test_32_add_product_bad_data(self):
        url = self.domain + "/freezers/" + self.token
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.post(url,
                          data=json.dumps(dict(product_name="name",
                                               text_descr="description",
                                               freezer_id=1,
                                               type_id=1,
                                               date_in='2016-03-05',
                                               period=21,
                                               box_num=1,
                                               prod_num=15,
                                               quantity=2)),
                          headers=headers)
        self.assertEqual(r.status_code, 400)
        content = r.json()
        self.assertEqual(content['details'], responseMessage.BAD_FORMAT)

    # add a correct product can be essentially done with the external website
    # That is why test test are not done here

    # UPDATE A PRODUCT
    def test_33_update_product_methods_not_implemented(self):
        self.methods_not_implemented("update_product/1/1/1/1", ['GET', 'PUT', 'DELETE'])

    def test_34_update_product_bad_content_type(self):
        url = self.domain + "/update_product/1/1/1/1/" + self.token
        r = requests.post(url,
                          data=json.dumps(dict(product_name="name",
                                               text_descr="description",
                                               freezer_id=1,
                                               type_id=1,
                                               date_in='2016-03-05',
                                               date_out='2016-03-05',
                                               period=21,
                                               box_num=1,
                                               prod_num=15,
                                               quantity=2)))
        self.assertEqual(r.status_code, 415)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
