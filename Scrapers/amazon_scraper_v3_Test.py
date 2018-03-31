from amazon_scraper_v3 import AmzonParser

testURLs = ['https://www.amazon.ca/Apple-iPhone-Factory-Unlocked-Phone/dp/B01N6YAP98/ref=sr_1_4?s=wireless&ie=UTF8&qid=1522509266&sr=1-4&keywords=iphone+7',
            'https://www.amazon.ca/Apple-iPhone-Factory-Unlocked-Smartphone/dp/B0743HPQVB/ref=sr_1_7?s=electronics&ie=UTF8&qid=1522509852&sr=1-7&keywords=iphone+7+plus',
            'https://www.amazon.ca/Apple-iPhone-6S-64GB-Refurbished/dp/B01CR1AA90/ref=sr_1_4?s=electronics&ie=UTF8&qid=1522509914&sr=1-4&keywords=iphone+6s',
            'https://www.amazon.ca/Apple-iPhone-64GB-Space-Unlocked/dp/B00NK332DG/ref=sr_1_4?s=electronics&ie=UTF8&qid=1522509948&sr=1-4&keywords=iphone+6',
            'https://www.amazon.ca/Samsung-Galaxy-Unlocked-Phone-SM-G950U/dp/B071NCHF1S/ref=sr_1_3?ie=UTF8&qid=1522527828&sr=8-3&keywords=samsung+8']

testData1 = AmzonParser(testURLs[0])
testData2 = AmzonParser(testURLs[1])
testData3 = AmzonParser(testURLs[2])
testData4 = AmzonParser(testURLs[3])
testData5 = AmzonParser(testURLs[4])

# print testData1
# print testData2cd 
# print testData3
# print testData4
# print testData5

# print "ePLATFORM = '%s'" % (testData5['PLATFORM'])
# print "eITEM_ID = '%s'" % (testData5['ITEM_ID'])
# print "eCARRIER = '%s'" % (testData5['CARRIER'])
# print "eTITLE = '%s'" % (testData5['TITLE'])
# print "eURL = '%s'" % (testData5['URL'])
# print "ePRICE = '%s'" % (testData5['PRICE'])
# print "eMEMORY = '%s'" % (testData5['MEMORY'])
# print "eMODEL = '%s'" % (testData5['MODEL'])
# print "eSHIPPING = '%s'" % (testData5['SHIPPING'])
# print "eDATE_POSTED = '%s'" % (testData5['DATE_POSTED'])

def checkTest1(dataset):
    print 'Checking data set 1...'
    correct = 0
    #our expected answers
    ePLATFORM = 'Amazon'
    eITEM_ID = 'B01N6YAP98'
    eCARRIER = 'Unlocked'
    eTITLE = 'Apple iPhone 7 Factory Unlocked Phone - 4.7Inch Screen - 32GB - Black (Certified Refurbished)'
    eURL = 'https://www.amazon.ca/Apple-iPhone-Factory-Unlocked-Phone/dp/B01N6YAP98/ref=sr_1_4?s=wireless&ie=UTF8&qid=1522509266&sr=1-4&keywords=iphone+7'
    ePRICE = '559.95'
    eMEMORY = '32GB'
    eMODEL = 'B01N6YAP98'
    eSHIPPING = None
    eDATE_POSTED = 'Feb. 14 2017'

    # check expected against actual
    if ePLATFORM == testData1['PLATFORM']:
        correct += 1
    else:
        print 'unexpected platform'
    if eITEM_ID == testData1['ITEM_ID']:
        correct += 1
    else:
        print 'unexpected item id'
    if eCARRIER == testData1['CARRIER']:
        correct += 1
    else:
        print 'unexpected carrier'
    if eTITLE == testData1['TITLE']:
        correct += 1
    else:
        print 'unexpected title'
    if eURL == testData1['URL']:
        correct += 1
    else:
        print 'unexpected url'
    if ePRICE == testData1['PRICE']:
        correct += 1
    else:
        print 'unexpected price'
    if eMEMORY == testData1['MEMORY']:
        correct += 1
    else:
        print 'unexpected memory'
    if eMODEL == testData1['MODEL']:
        correct += 1
    else:
        print 'unexpected model'
    if eSHIPPING == testData1['SHIPPING']:
        correct += 1
    else:
        print 'unexpected shipping'
    if eDATE_POSTED == testData1['DATE_POSTED']:
        correct += 1
    else:
        print 'unexpected data posted'

    return correct

def checkTest2(dataset):
    print 'Checking data set 2...'
    correct = 0

    ePLATFORM = 'Amazon'
    eITEM_ID = 'B0743HPQVB'
    eCARRIER = 'Unlocked'
    eTITLE = 'Apple iPhone 7 Plus Factory Unlocked CDMA/GSM Smartphone - (Certified Refurbished) (128GB, Jet Black)'
    eURL = 'https://www.amazon.ca/Apple-iPhone-Factory-Unlocked-Smartphone/dp/B0743HPQVB/ref=sr_1_7?s=electronics&ie=UTF8&qid=1522509852&sr=1-7&keywords=iphone+7+plus'
    ePRICE = '847.99'
    eMEMORY = '(128GB,'
    eMODEL = 'IPHONE7-PLUS-B1-MP'
    eSHIPPING = None
    eDATE_POSTED = 'Feb. 17 2017'

    # check expected against actual
    if ePLATFORM == testData2['PLATFORM']:
        correct += 1
    else:
        print 'unexpected platform'
    if eITEM_ID == testData2['ITEM_ID']:
        correct += 1
    else:
        print 'unexpected item id'
    if eCARRIER == testData2['CARRIER']:
        correct += 1
    else:
        print 'unexpected carrier'
    if eTITLE == testData2['TITLE']:
        correct += 1
    else:
        print 'unexpected title'
    if eURL == testData2['URL']:
        correct += 1
    else:
        print 'unexpected url'
    if ePRICE == testData2['PRICE']:
        correct += 1
    else:
        print 'unexpected price'
    if eMEMORY == testData2['MEMORY']:
        correct += 1
    else:
        print 'unexpected memory'
    if eMODEL == testData2['MODEL']:
        correct += 1
    else:
        print 'unexpected model'
    if eSHIPPING == testData2['SHIPPING']:
        correct += 1
    else:
        print 'unexpected shipping'
    if eDATE_POSTED == testData2['DATE_POSTED']:
        correct += 1
    else:
        print 'unexpected data posted'

    return correct
def checkTest3(dataset):
    print 'Checking data set 3...'
    correct = 0

    ePLATFORM = 'Amazon'
    eITEM_ID = 'B01CR1AA90'
    eCARRIER = 'Unlocked'
    eTITLE = 'Apple iPhone 6S 64GB - GSM Unlocked - Space Gray (Certified Refurbished)'
    eURL = 'https://www.amazon.ca/Apple-iPhone-6S-64GB-Refurbished/dp/B01CR1AA90/ref=sr_1_4?s=electronics&ie=UTF8&qid=1522509914&sr=1-4&keywords=iphone+6s'
    ePRICE = '368.00'
    eMEMORY = '64GB'
    eMODEL = '6S'
    eSHIPPING = None
    eDATE_POSTED = 'Oct. 4 2016'

    # check expected against actual
    if ePLATFORM == testData3['PLATFORM']:
        correct += 1
    else:
        print 'unexpected platform'
    if eITEM_ID == testData3['ITEM_ID']:
        correct += 1
    else:
        print 'unexpected item id'
    if eCARRIER == testData3['CARRIER']:
        correct += 1
    else:
        print 'unexpected carrier'
    if eTITLE == testData3['TITLE']:
        correct += 1
    else:
        print 'unexpected title'
    if eURL == testData3['URL']:
        correct += 1
    else:
        print 'unexpected url'
    if ePRICE == testData3['PRICE']:
        correct += 1
    else:
        print 'unexpected price'
    if eMEMORY == testData3['MEMORY']:
        correct += 1
    else:
        print 'unexpected memory'
    if eMODEL == testData3['MODEL']:
        correct += 1
    else:
        print 'unexpected model'
    if eSHIPPING == testData3['SHIPPING']:
        correct += 1
    else:
        print 'unexpected shipping'
    if eDATE_POSTED == testData3['DATE_POSTED']:
        correct += 1
    else:
        print 'unexpected data posted'

    return correct
def checkTest4(dataset):
    print 'Checking data set 4...'
    correct = 0

    ePLATFORM = 'Amazon'
    eITEM_ID = 'B00NK332DG'
    eCARRIER = 'Unlocked'
    eTITLE = 'Apple iPhone 6 64GB (Space Grey) Unlocked'
    eURL = 'https://www.amazon.ca/Apple-iPhone-64GB-Space-Unlocked/dp/B00NK332DG/ref=sr_1_4?s=electronics&ie=UTF8&qid=1522509948&sr=1-4&keywords=iphone+6'
    ePRICE = '518.57'
    eMEMORY = '64GB'
    eMODEL = 'A1549'
    eSHIPPING = None
    eDATE_POSTED = 'Oct. 24 2014'

    # check expected against actual
    if ePLATFORM == testData4['PLATFORM']:
        correct += 1
    else:
        print 'unexpected platform'
    if eITEM_ID == testData4['ITEM_ID']:
        correct += 1
    else:
        print 'unexpected item id'
    if eCARRIER == testData4['CARRIER']:
        correct += 1
    else:
        print 'unexpected carrier'
    if eTITLE == testData4['TITLE']:
        correct += 1
    else:
        print 'unexpected title'
    if eURL == testData4['URL']:
        correct += 1
    else:
        print 'unexpected url'
    if ePRICE == testData4['PRICE']:
        correct += 1
    else:
        print 'unexpected price'
    if eMEMORY == testData4['MEMORY']:
        correct += 1
    else:
        print 'unexpected memory'
    if eMODEL == testData4['MODEL']:
        correct += 1
    else:
        print 'unexpected model'
    if eSHIPPING == testData4['SHIPPING']:
        correct += 1
    else:
        print 'unexpected shipping'
    if eDATE_POSTED == testData4['DATE_POSTED']:
        correct += 1
    else:
        print 'unexpected data posted'

    return correct
def checkTest5(dataset):
    print 'Checking data set 5...'
    correct = 0

    ePLATFORM = 'Amazon'
    eITEM_ID = 'B071NCHF1S'
    eCARRIER = 'Unlocked'
    eTITLE = 'Samsung Galaxy S8, G950FD 64GB Smartphone, Midnight Black, Factory Unlocked (International Version)'
    eURL = 'https://www.amazon.ca/Samsung-Galaxy-Unlocked-Phone-SM-G950U/dp/B071NCHF1S/ref=sr_1_3?ie=UTF8&qid=1522527828&sr=8-3&keywords=samsung+8'
    ePRICE = '799.99'
    eMEMORY = '64GB'
    eMODEL = 'SM-SAMG950FDBLKEU'
    eSHIPPING = None
    eDATE_POSTED = 'April 19 2017'

    # check expected against actual
    if ePLATFORM == testData5['PLATFORM']:
        correct += 1
    else:
        print 'unexpected platform'
    if eITEM_ID == testData5['ITEM_ID']:
        correct += 1
    else:
        print 'unexpected item id'
    if eCARRIER == testData5['CARRIER']:
        correct += 1
    else:
        print 'unexpected carrier'
    if eTITLE == testData5['TITLE']:
        correct += 1
    else:
        print 'unexpected title'
    if eURL == testData5['URL']:
        correct += 1
    else:
        print 'unexpected url'
    if ePRICE == testData5['PRICE']:
        correct += 1
    else:
        print 'unexpected price'
    if eMEMORY == testData5['MEMORY']:
        correct += 1
    else:
        print 'unexpected memory'
    if eMODEL == testData5['MODEL']:
        correct += 1
    else:
        print 'unexpected model'
    if eSHIPPING == testData5['SHIPPING']:
        correct += 1
    else:
        print 'unexpected shipping'
    if eDATE_POSTED == testData5['DATE_POSTED']:
        correct += 1
    else:
        print 'unexpected data posted'

    return correct

test1 = checkTest1(testData1)
test2 = checkTest2(testData2)
test3 = checkTest3(testData3)
test4 = checkTest4(testData4)
test5 = checkTest5(testData5)
if test1 == 10:
    print 'test 1 returns 10/10'
else:
    print 'test 1 returns %d/10' % (test1)
if test2 == 10:
    print 'test 2 returns 10/10'
else:
    print 'test 2 returns %d/10' % (test2)
if test3 == 10:
    print 'test 3 returns 10/10'
else:
    print 'test 3 returns %d/10' % (test3)
if test4 == 10:
    print 'test 4 returns 10/10'
else:
    print 'test 4 returns %d/10' % (test4)
if test5 == 10:
    print 'test 5 returns 10/10'
else:
    print 'test 5 returns %d/10' % (test5)