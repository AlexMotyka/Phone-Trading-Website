import json
import unittest
from eBay_v2 import parse_url
from HTMLTestRunner import HTMLTestRunner


'''
# This block is to load json file
data = {}
with open('eBay-Scraped-Data.json') as json_data:
    d = json.load(json_data)
    # print(d)
    i = 0
    for item in d:
        data[i] = {
            'TITLE': item.get("TITLE"),
            'URL': item.get("URL"),
            'ADDRESS': item.get("ADDRESS"),
            'VISITS': item.get("VISITS"),
            'POSTER_ID': item.get("POSTER_ID"),
            'CARRIER': item.get("CARRIER"),
            'ITEM_ID': item.get("ITEM_ID"),
            'MODEL': item.get("MODEL"),
            'PRICE': item.get("PRICE"),
            'PLATFORM': item.get("PLATFORM"),
            'MEMORY': item.get("MEMORY")
        }
        # print(data[i])
        i = i + 1
'''

# This block is to use parse_url
data = parse_url('&Brand=Apple&Model=iPhone%2520X')

# print('Collected Data: ')
# print('    > ' + str(data))


class TestItemOneCorrectness(unittest.TestCase):

    def test_title(self):
        self.assertEqual(data[0]['TITLE'], 'Apple iPhone 6 32GB Unlocked Gray/Silver Smartphone *z (Canadian Model)')

    def test_url(self):
        self.assertEqual(data[0]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-6-32GB-Unlocked-Gray-Silver-Smartphone-z-Canadian-Model/263510386154?hash=item3d5a7165ea:m:mTffahPjkJNHY8MtZCjg_ig')

    def test_address(self):
        self.assertEqual(data[0]['ADDRESS'], 'Markham, ON, Canada')

    def test_visits(self):
        self.assertEqual(data[0]['VISITS'], '111+ Sold')

    def test_poster_id(self):
        self.assertEqual(data[0]['POSTER_ID'], 'gadgetag')

    def test_carrier(self):
        self.assertEqual(data[0]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        self.assertEqual(data[0]['ITEM_ID'], '263510386154')

    def test_model(self):
        self.assertEqual(data[0]['MODEL'], 'iPhone 6')

    def test_price(self):
        self.assertEqual(data[0]['PRICE'], 269.99)

    def test_platform(self):
        self.assertEqual(data[0]['PLATFORM'], 'ebay')

    def test_memory(self):
        self.assertEqual(data[0]['MEMORY'], '32')


class TestItemTwoCorrectness(unittest.TestCase):

    def test_title(self):
        self.assertEqual(data[1]['TITLE'], 'Apple iPhone 6 16GB Canadian Model Unlocked Multiple Color 4G LTE Smartphone *y')

    def test_url(self):
        self.assertEqual(data[1]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-6-16GB-Canadian-Model-Unlocked-Multiple-Color-4G-LTE-Smartphone-y/263562924747?hash=item3d5d9312cb:m:mkvj9X9Rk6jBWVH6_n_Em8g')

    def test_address(self):
        self.assertEqual(data[1]['ADDRESS'], 'Markham, ON, Canada')

    def test_visits(self):
        self.assertEqual(data[1]['VISITS'], '15+ Watching')

    def test_poster_id(self):
        self.assertEqual(data[1]['POSTER_ID'], 'gadgetag')

    def test_carrier(self):
        self.assertEqual(data[1]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        self.assertEqual(data[1]['ITEM_ID'], '263562924747')

    def test_model(self):
        self.assertEqual(data[1]['MODEL'], 'iPhone 6')

    def test_price(self):
        self.assertEqual(data[1]['PRICE'], 219.99)

    def test_platform(self):
        self.assertEqual(data[1]['PLATFORM'], 'ebay')

    def test_memory(self):
        self.assertEqual(data[1]['MEMORY'], '16')


class TestPlatform(unittest.TestCase):

    def test_platform(self):
        for i in data:
            self.assertEqual(data[i]['PLATFORM'], 'ebay')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemOneCorrectness))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemTwoCorrectness))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPlatform))
    with open('eBay_Test_Report.html', 'w') as f:
        runner = HTMLTestRunner(stream=f, title='eBay Test Report', description='Powered by HTMLTestRunner', verbosity=2)
        runner.run(suite)
    print('Testing: ')
    print('    > eBay_Test_Report.html is generated')
