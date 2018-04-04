import json
import unittest
from eBay_v2 import parse_url
from HTMLTestRunner import HTMLTestRunner


def read_json():
    """This is to load json file"""
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
    # print('Collected Data: ')
    # print('    > ' + str(data))


"""Load data either use parse_url() to fetch or read from eBay-Scraped-Data.json"""
# This is to use parse_url from eBay_v2
data = parse_url('&Brand=Apple&Model=iPhone%2520X')

# This is to use read_json to load data
# data = {}
# read_json()


class TestKeyword(unittest.TestCase):

    def test_title_keyword(self):
        """Pass if iPhone in TITLE"""
        for i in data:
            self.assertIn('iphone', data[i]['TITLE'].lower())

    def test_url_keyword(self):
        """Pass if https://www.ebay.ca/itm in URL"""
        for i in data:
            self.assertIn('https://www.ebay.ca/itm', data[i]['URL'])

    def test_platform_keyword(self):
        """Pass if PLATFORM is eBay"""
        for i in data:
            self.assertEqual(data[i]['PLATFORM'], 'ebay')


class TestKeywordFilter(unittest.TestCase):

    def test_title_keyword_filter(self):
        """Pass if keywords not in TITLE"""
        for i in data:
            for keyword in ["parts", "fake", "broken", "damaged", "cracked"]:
                self.assertNotIn(keyword, data[i]['TITLE'].lower())

    def test_url_keyword_filter(self):
        """Pass if pulsar.ebay.ca not in URL"""
        for i in data:
            self.assertNotIn('pulsar.ebay.ca', data[i]['URL'])

    def test_carrier_keyword_filter(self):
        """Pass if Choose your carrier not in CARRIER"""
        for i in data:
            self.assertNotIn('choose your carrier', data[i]['CARRIER'].lower())

    def test_memory_keyword_filter(self):
        """Pass if Gb or / not in MEMORY"""
        for i in data:
            for keyword in ["gb", "/"]:
                self.assertNotIn(keyword, data[i]['MEMORY'].lower())


class TestPrice(unittest.TestCase):

    def test_price_float_type(self):
        """Pass if PRICE is float type"""
        for i in data:
            self.assertIsInstance(data[i]['PRICE'], float)

    def test_price_not_null(self):
        """Pass if PRICE is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['PRICE'], "")

    def test_price_larger_equal_than_100(self):
        """Pass if PRICE is larger or equal than 100"""
        for i in data:
            self.assertGreaterEqual(data[i]['PRICE'], 100)


class TestNotNULL(unittest.TestCase):

    def test_title_not_null(self):
        """Pass if TITLE is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['TITLE'], "")

    def test_url_not_null(self):
        """Pass if URL is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['URL'], "")

    def test_poster_ID_not_null(self):
        """Pass if POSTER_ID is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['POSTER_ID'], "")

    def test_item_ID_not_null(self):
        """Pass if ITEM_ID is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['ITEM_ID'], "")

    def test_price_not_null(self):
        """Pass if PRICE is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['PRICE'], "")

    def test_platform_not_null(self):
        """Pass if PLATFORM is not NULL"""
        for i in data:
            self.assertNotEqual(data[i]['PLATFORM'], "")


class TestItemCorrectness1(unittest.TestCase):

    @staticmethod
    def search_index():
        """Find the correct index"""
        for i in data:
            if data[i]['TITLE'] == 'Apple iPhone 6 32GB Unlocked Gray/Silver Smartphone *z (Canadian Model)':
                return i

    def test_title(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['TITLE'], 'Apple iPhone 6 32GB Unlocked Gray/Silver Smartphone *z (Canadian Model)')

    def test_url(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-6-32GB-Unlocked-Gray-Silver-Smartphone-z-Canadian-Model/263510386154?hash=item3d5a7165ea:m:mTffahPjkJNHY8MtZCjg_ig')

    def test_address(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ADDRESS'], 'Markham, ON, Canada')

    '''
    def test_visits(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['VISITS'], '111+ Sold')
    '''

    def test_poster_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['POSTER_ID'], 'gadgetag')

    def test_carrier(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ITEM_ID'], '263510386154')

    def test_model(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MODEL'], 'iPhone 6')

    def test_price(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PRICE'], 269.99)

    def test_platform(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PLATFORM'], 'ebay')

    def test_memory(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MEMORY'], '32')


class TestItemCorrectness2(unittest.TestCase):

    @staticmethod
    def search_index():
        """Find the correct index"""
        for i in data:
            if data[i]['TITLE'] == 'Apple iPhone 6 16GB Canadian Model Unlocked Multiple Color 4G LTE Smartphone *y':
                return i

    def test_title(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['TITLE'], 'Apple iPhone 6 16GB Canadian Model Unlocked Multiple Color 4G LTE Smartphone *y')

    def test_url(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-6-16GB-Canadian-Model-Unlocked-Multiple-Color-4G-LTE-Smartphone-y/263562924747?hash=item3d5d9312cb:m:mkvj9X9Rk6jBWVH6_n_Em8g')

    def test_address(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ADDRESS'], 'Markham, ON, Canada')

    '''
    def test_visits(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['VISITS'], '15+ Watching')
    '''

    def test_poster_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['POSTER_ID'], 'gadgetag')

    def test_carrier(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ITEM_ID'], '263562924747')

    def test_model(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MODEL'], 'iPhone 6')

    def test_price(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PRICE'], 219.99)

    def test_platform(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PLATFORM'], 'ebay')

    def test_memory(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MEMORY'], '16')


class TestItemCorrectness3(unittest.TestCase):

    @staticmethod
    def search_index():
        """Find the correct index"""
        for i in data:
            if data[i]['TITLE'] == 'Apple iPhone 7 32gb GSM Unlocked Smartphone':
                return i

    def test_title(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['TITLE'], 'Apple iPhone 7 32gb GSM Unlocked Smartphone')

    def test_url(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-7-32gb-GSM-Unlocked-Smartphone/272714391407?hash=item3f7f0b5f6f:m:mWgYDe4a79NeLuAlV-RmAQA')

    def test_address(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ADDRESS'], 'Montreal, QC , Canada')

    '''
    def test_visits(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['VISITS'], '81+ Sold')
    '''

    def test_poster_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['POSTER_ID'], 'wireless.canada')

    def test_carrier(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ITEM_ID'], '272714391407')

    def test_model(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MODEL'], 'iPhone 7')

    def test_price(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PRICE'], 449.99)

    def test_platform(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PLATFORM'], 'ebay')

    def test_memory(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MEMORY'], '32')


class TestItemCorrectness4(unittest.TestCase):

    @staticmethod
    def search_index():
        """Find the correct index"""
        for i in data:
            if data[i]['TITLE'] == 'Apple iPhone 6 64GB Canadian Model Gray 4G unlocked LTE Smartphone *z':
                return i

    def test_title(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['TITLE'], 'Apple iPhone 6 64GB Canadian Model Gray 4G unlocked LTE Smartphone *z')

    def test_url(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['URL'], 'https://www.ebay.ca/itm/Apple-iPhone-6-64GB-Canadian-Model-Gray-4G-unlocked-LTE-Smartphone-z/263494504885?hash=item3d597f11b5:m:mkvj9X9Rk6jBWVH6_n_Em8g')

    def test_address(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ADDRESS'], 'Markham, ON, Canada')

    '''
    def test_visits(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['VISITS'], '15+ Sold')
    '''

    def test_poster_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['POSTER_ID'], 'gadgetag')

    def test_carrier(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['CARRIER'], 'Unlocked')

    def test_item_id(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['ITEM_ID'], '263494504885')

    def test_model(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MODEL'], 'iPhone 6')

    def test_price(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PRICE'], 289.99)

    def test_platform(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['PLATFORM'], 'ebay')

    def test_memory(self):
        """Test exact match"""
        self.assertEqual(data[self.search_index()]['MEMORY'], '64')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestKeyword))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestKeywordFilter))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPrice))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNotNULL))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemCorrectness1))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemCorrectness2))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemCorrectness3))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestItemCorrectness4))
    with open('eBay_Test_Report.html', 'w') as f:
        runner = HTMLTestRunner(stream=f, title='eBay Test Report', description='Powered by HTMLTestRunner', verbosity=2)
        runner.run(suite)
        print('Testing: ')
        print('    > eBay_Test_Report.html is generated')
