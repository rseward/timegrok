#!/usr/bin/env python

"""
Unit test for identifying numeric quantities.

Need to run this for some reason. See if this can triggered by code?
   python -m spacy download en_core_web_sm

pip install spacy word2num
"""

import datetime
import unittest

from timegrok.timegrok import TimeInterpreter, TimeUnit



class TestTimeStrings(unittest.TestCase):

    def doTest(self, timestr, curtime=None, expectTime=False):
        groker = TimeInterpreter()
        ret = groker.grok( timestr, curtime)
        print(ret)
        if expectTime:
            assert ret is not None, f"TimeGrok should return a time from '{timestr}'"
        else:
            assert ret is None, f"TimeGrok not expected to return a time for '{timestr}'"
            
        return ret

    @unittest.skip("Focus, rob, focus!")
    def testTenMinutes(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In ten minutes", curtime, expectTime=True )
        res2 = self.doTest( "In 10 minutes", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (10*60-1), "TimeGrok comprehended less than 10 minutes"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testSixtySeconds(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In sixty seconds", curtime, expectTime=True)
        res2 = self.doTest( "In 60 seconds", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (1*60-1), "TimeGrok comprehended less than 1 minute"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testFiveDays(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In five days", curtime, expectTime=True)
        res2 = self.doTest( "In 5 days", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (5*TimeUnit.DAY.value-1), "TimeGrok comprehended less than 5 days"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testSevenWeeks(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In seven weeks", curtime, expectTime=True)
        res2 = self.doTest( "In 7 weeks", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (7*TimeUnit.WEEK.value-1), "TimeGrok comprehended less than 5 days"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testTwoMonths(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In two months", curtime, expectTime=True)
        res2 = self.doTest( "In 2 months", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (2*TimeUnit.MONTH.value-1), "TimeGrok comprehended less than 2 months"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testOneYear(self):
        curtime = datetime.datetime.now()
        #res = self.doTest( "I bought 10 apples for $5.99" )
        #res = self.doTest( "I bought ten apples for $5.99" )        
        res1 = self.doTest( "In one year", curtime, expectTime=True)
        res2 = self.doTest( "In 1 year", curtime, expectTime=True)

        # Results should be equivalent
        assert (res1 - curtime).total_seconds() > (1*TimeUnit.YEAR.value-1), "TimeGrok comprehended less than 1 year"
        assert res1 == res2, f"Both time expression should evaluate to the same time. {res1=} != {res2=}"

    @unittest.skip("Focus, rob, focus!")
    def testMissingQuantity(self):
        curtime = datetime.datetime.now()
        self.doTest( "In a minute", curtime, expectTime=True)

    def testAtSpecifiedTime(self):
        now=datetime.datetime.now()
        # Morning for later in the morning
        curtime=morning=datetime.datetime( now.year, now.month, now.day, 6, 0)
        res1 = self.doTest( "At 07:45 AM", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 07:45", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 3:30", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 1:00PM", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        assert abs((res1 - curtime).total_seconds())< 7.5 * 60*60, f"Expected TimeGrok to return a time at approximately 1PM! {res1=} > {curtime=}"
        res1 = self.doTest( "At 1PM", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        assert abs((res1 - curtime).total_seconds())< 7.5 * 60*60, f"Expected TimeGrok to return a time at approximately 1PM! {res1=} > {curtime=}"
        res1 = self.doTest( "At 4AM", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        
        # Afternoon for tomorrow morning
        curtime=afternoon=datetime.datetime( now.year, now.month, now.day, 19, 30)
        res1 = self.doTest( "At 07:45 AM", afternoon, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 07:45", afternoon, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"

        # Afternoon/evening for tomorrow afternoon        
        res1 = self.doTest( "At 01:00 PM", afternoon, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 01:00", afternoon, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"

        # Morning for this afternoon
        curtime=morning
        res1 = self.doTest( "At 03:30 PM", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At 03:30", morning, expectTime=True)
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"        

        # Time words
        res1 = self.doTest( "At noon", morning, expectTime=True)        
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At midnight", morning, expectTime=True)        
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"
        res1 = self.doTest( "At dawn", morning, expectTime=True)        
        assert res1 > curtime, f"Expected TimeGrok to return a time in the future! {res1=} > {curtime=}"                

    @unittest.skip("Focus, rob, focus!")
    def testGibberish(self):
        self.doTest( "In one soup", expectTime=False )
        self.doTest( "In a jiffy", expectTime=False )
        self.doTest( "blah", expectTime=False )

        



if __name__ == "__main__":
    unittest.main()
