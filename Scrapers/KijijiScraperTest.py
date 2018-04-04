from kijijiscraper import geturllist, getitemurl, iteminfo
import unittest
import ast


f=open("searchpage.html", 'r')
searchpage = f.read()
f.close

f = open("pagelinks" ,"r")
pagelinks = f.read()
f.close

f = open("phonelinks" ,"r")
phonelinks = f.read()
f.close

phones_raw=[]
phones_expected = []
for i in range(5):
    f = open("phone_%d" %(i+1), 'r')
    phones_raw.append(f.read())
    f.close()

phonedict = []

for i in range(5):
    f = open("phone_%d_expected" %(i+1), 'r')
    phones_expected.append(ast.literal_eval(f.read()))
    f.close()
    phonedict.append(iteminfo(testing=True, html=phones_raw[i]))



urllisttestdata = geturllist(testing=True,html=searchpage)

itemtestdata = getitemurl(testing=True,html=searchpage)

# phonedict = iteminfo(testing=True, html=phones_raw[0])



class testPageGen(unittest.TestCase):

    def test_pages(self):
        self.assertEqual(pagelinks,str(urllisttestdata))

    def test_link(self):
        self.assertEqual(phonelinks,str(itemtestdata))

class testDataScraper1(unittest.TestCase):

    def test_Platform(self):
        self.assertEqual(phones_expected[0]["PLATFORM"], phonedict[0]["PLATFORM"])

    def test_Title(self):
        self.assertEqual(phones_expected[0]["TITLE"], phonedict[0]["TITLE"])

    def test_Date(self):
        self.assertEqual(phones_expected[0]["DATE_POSTED"], phonedict[0]["DATE_POSTED"])

    def test_Latitude(self):
        self.assertEqual(phones_expected[0]["LATITUDE"], phonedict[0]["LATITUDE"])

    def test_Longitude(self):
        self.assertEqual(phones_expected[0]["LONGITUDE"], phonedict[0]["LONGITUDE"])

    def test_Address(self):
        self.assertEqual(phones_expected[0]["ADDRESS"], phonedict[0]["ADDRESS"])

    def test_Poster_ID(self):
        self.assertEqual(phones_expected[0]["POSTER_ID"], phonedict[0]["POSTER_ID"])

    def test_Description(self):
        self.assertEqual(phones_expected[0]["DESCRIPTION"], phonedict[0]["DESCRIPTION"])

    def test_ItemID(self):
        self.assertEqual(phones_expected[0]["ITEM_ID"], phonedict[0]["ITEM_ID"])

    def test_Visits(self):
        self.assertEqual(phones_expected[0]["VISITS"], phonedict[0]["VISITS"])

    def test_Selltype(self):
        self.assertEqual(phones_expected[0]["SELLTYPE"], phonedict[0]["SELLTYPE"])

    def test_Price(self):
        self.assertEqual(phones_expected[0]["PRICE"], phonedict[0]["PRICE"])

    def test_Adtype(self):
        self.assertEqual(phones_expected[0]["ADTYPE"], phonedict[0]["ADTYPE"])

class testDataScraper2(unittest.TestCase):

    def test_Platform(self):
        self.assertEqual(phones_expected[1]["PLATFORM"], phonedict[1]["PLATFORM"])

    def test_Title(self):
        self.assertEqual(phones_expected[1]["TITLE"], phonedict[1]["TITLE"])

    def test_Date(self):
        self.assertEqual(phones_expected[1]["DATE_POSTED"], phonedict[1]["DATE_POSTED"])

    def test_Latitude(self):
        self.assertEqual(phones_expected[1]["LATITUDE"], phonedict[1]["LATITUDE"])

    def test_Longitude(self):
        self.assertEqual(phones_expected[1]["LONGITUDE"], phonedict[1]["LONGITUDE"])

    def test_Address(self):
        self.assertEqual(phones_expected[1]["ADDRESS"], phonedict[1]["ADDRESS"])

    def test_Poster_ID(self):
        self.assertEqual(phones_expected[1]["POSTER_ID"], phonedict[1]["POSTER_ID"])

    def test_Description(self):
        self.assertEqual(phones_expected[1]["DESCRIPTION"], phonedict[1]["DESCRIPTION"])

    def test_ItemID(self):
        self.assertEqual(phones_expected[1]["ITEM_ID"], phonedict[1]["ITEM_ID"])

    def test_Visits(self):
        self.assertEqual(phones_expected[1]["VISITS"], phonedict[1]["VISITS"])

    def test_Selltype(self):
        self.assertEqual(phones_expected[1]["SELLTYPE"], phonedict[1]["SELLTYPE"])

    def test_Price(self):
        self.assertEqual(phones_expected[1]["PRICE"], phonedict[1]["PRICE"])

    def test_Adtype(self):
        self.assertEqual(phones_expected[1]["ADTYPE"], phonedict[1]["ADTYPE"])

class testDataScraper3(unittest.TestCase):

    def test_Platform(self):
        self.assertEqual(phones_expected[2]["PLATFORM"], phonedict[2]["PLATFORM"])

    def test_Title(self):
        self.assertEqual(phones_expected[2]["TITLE"], phonedict[2]["TITLE"])

    def test_Date(self):
        self.assertEqual(phones_expected[2]["DATE_POSTED"], phonedict[2]["DATE_POSTED"])

    def test_Latitude(self):
        self.assertEqual(phones_expected[2]["LATITUDE"], phonedict[2]["LATITUDE"])

    def test_Longitude(self):
        self.assertEqual(phones_expected[2]["LONGITUDE"], phonedict[2]["LONGITUDE"])

    def test_Address(self):
        self.assertEqual(phones_expected[2]["ADDRESS"], phonedict[2]["ADDRESS"])

    def test_Poster_ID(self):
        self.assertEqual(phones_expected[2]["POSTER_ID"], phonedict[2]["POSTER_ID"])

    def test_Description(self):
        self.assertEqual(phones_expected[2]["DESCRIPTION"], phonedict[2]["DESCRIPTION"])

    def test_ItemID(self):
        self.assertEqual(phones_expected[2]["ITEM_ID"], phonedict[2]["ITEM_ID"])

    def test_Visits(self):
        self.assertEqual(phones_expected[2]["VISITS"], phonedict[2]["VISITS"])

    def test_Selltype(self):
        self.assertEqual(phones_expected[2]["SELLTYPE"], phonedict[2]["SELLTYPE"])

    def test_Price(self):
        self.assertEqual(phones_expected[2]["PRICE"], phonedict[2]["PRICE"])

    def test_Adtype(self):
        self.assertEqual(phones_expected[2]["ADTYPE"], phonedict[2]["ADTYPE"])


class testDataScraper4(unittest.TestCase):

    def test_Platform(self):
        self.assertEqual(phones_expected[3]["PLATFORM"], phonedict[3]["PLATFORM"])

    def test_Title(self):
        self.assertEqual(phones_expected[3]["TITLE"], phonedict[3]["TITLE"])

    def test_Date(self):
        self.assertEqual(phones_expected[3]["DATE_POSTED"], phonedict[3]["DATE_POSTED"])

    def test_Latitude(self):
        self.assertEqual(phones_expected[3]["LATITUDE"], phonedict[3]["LATITUDE"])

    def test_Longitude(self):
        self.assertEqual(phones_expected[3]["LONGITUDE"], phonedict[3]["LONGITUDE"])

    def test_Address(self):
        self.assertEqual(phones_expected[3]["ADDRESS"], phonedict[3]["ADDRESS"])

    def test_Poster_ID(self):
        self.assertEqual(phones_expected[3]["POSTER_ID"], phonedict[3]["POSTER_ID"])

    def test_Description(self):
        self.assertEqual(phones_expected[3]["DESCRIPTION"], phonedict[3]["DESCRIPTION"])

    def test_ItemID(self):
        self.assertEqual(phones_expected[3]["ITEM_ID"], phonedict[3]["ITEM_ID"])

    def test_Visits(self):
        self.assertEqual(phones_expected[3]["VISITS"], phonedict[3]["VISITS"])

    def test_Selltype(self):
        self.assertEqual(phones_expected[3]["SELLTYPE"], phonedict[3]["SELLTYPE"])

    def test_Price(self):
        self.assertEqual(phones_expected[3]["PRICE"], phonedict[3]["PRICE"])

    def test_Adtype(self):
        self.assertEqual(phones_expected[3]["ADTYPE"], phonedict[3]["ADTYPE"])


class testDataScraper5(unittest.TestCase):

    def test_Platform(self):
        self.assertEqual(phones_expected[4]["PLATFORM"], phonedict[4]["PLATFORM"])

    def test_Title(self):
        self.assertEqual(phones_expected[4]["TITLE"], phonedict[4]["TITLE"])

    def test_Date(self):
        self.assertEqual(phones_expected[4]["DATE_POSTED"], phonedict[4]["DATE_POSTED"])

    def test_Latitude(self):
        self.assertEqual(phones_expected[4]["LATITUDE"], phonedict[4]["LATITUDE"])

    def test_Longitude(self):
        self.assertEqual(phones_expected[4]["LONGITUDE"], phonedict[4]["LONGITUDE"])

    def test_Address(self):
        self.assertEqual(phones_expected[4]["ADDRESS"], phonedict[4]["ADDRESS"])

    def test_Poster_ID(self):
        self.assertEqual(phones_expected[4]["POSTER_ID"], phonedict[4]["POSTER_ID"])

    def test_Description(self):
        self.assertEqual(phones_expected[4]["DESCRIPTION"], phonedict[4]["DESCRIPTION"])

    def test_ItemID(self):
        self.assertEqual(phones_expected[4]["ITEM_ID"], phonedict[4]["ITEM_ID"])

    def test_Visits(self):
        self.assertEqual(phones_expected[4]["VISITS"], phonedict[4]["VISITS"])

    def test_Selltype(self):
        self.assertEqual(phones_expected[4]["SELLTYPE"], phonedict[4]["SELLTYPE"])

    def test_Price(self):
        self.assertEqual(phones_expected[4]["PRICE"], phonedict[4]["PRICE"])

    def test_Adtype(self):
        self.assertEqual(phones_expected[4]["ADTYPE"], phonedict[4]["ADTYPE"])




unittest.main()
