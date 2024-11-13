#!/usr/bin/env python

import arrow
import unittest
import datetime

from timegrok.dategrok import DateInterpreter

"""
Interpret human date expersions like:

last monday
this monday
next monday

begining of month
end of month

compact date math expressions

1d  => tomorrow  
-1d => yesterday
+1w => 3 days from now
-1y => one year ago

"""

def isEmpty(val: str) -> bool:
    empty=False
    
    if val is None:
        empty=True
    if isinstance(val, str) and len(val)==0:
        empty=True
        
    return empty


class TestDateInterpreter(unittest.TestCase):

    def setUp(self):
        self.interpreter = DateInterpreter()
        pass

    def dotest(self, dstr, rd=None, expected=None):
        print( f"\n{dstr} -> ???" )
        if rd is not None:
            ret = self.interpreter.interpretRelativeToDate(dstr, rd)
        else:
            ret = self.interpreter.interpret(dstr)
        print( f"{dstr} -> {ret} [{expected}]" )
        assert ret is not None, "Expected a result not None!"

        if expected:
            assert expected.year == ret.year and \
                   expected.month == ret.month and \
                   expected.day == ret.day , \
                   f"Return for '{dstr}' doesn't match expected date relative_to_date={rd}, {ret=} != {expected=}"

    #@unittest.SkipTest
    def testLastExps1(self):
        #skip_tests = [  ]
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,14) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,15) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,16) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,17) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,18) }            
            ]
        rd=datetime.datetime(2024,5,21)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            


    #@unittest.SkipTest
    def testLastExps2(self):
        #skip_tests = [ ]
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,15) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,16) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,17) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,18) }
            ]
        rd=datetime.datetime(2024,5,22)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)

    #@unittest.SkipTest
    def testLastExps3(self):
        #skip_tests = [ ]
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,22) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,16) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,17) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,18) }
            ]
        rd=datetime.datetime(2024,5,23)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            

    #@unittest.SkipTest
    def testLastExps4(self):
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,22) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,23) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,17) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,18) }
            ]
        rd=datetime.datetime(2024,5,24)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            

    #@unittest.SkipTest
    def testLastExps5(self):
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,22) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,23) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,24) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,18) }
            ]
        rd=datetime.datetime(2024,5,25)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)

    #@unittest.SkipTest
    def testLastExps6(self):
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,19) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,22) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,23) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,24) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,25) }
            ]
        rd=datetime.datetime(2024,5,26)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)
            
            
    #@unittest.SkipTest
    def testLastExps7(self):
        #skip_tests = [ ]
        tests = [
                  { "exp": "last sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "last monday", "expected": datetime.datetime(2024,5,20) },
                  { "exp": "last tuesday", "expected": datetime.datetime(2024,5,21) },
                  { "exp": "last wednesday", "expected": datetime.datetime(2024,5,22) },
                  { "exp": "last thursday", "expected": datetime.datetime(2024,5,23) },
                  { "exp": "last friday", "expected": datetime.datetime(2024,5,24) },
                  { "exp": "last saturday", "expected": datetime.datetime(2024,5,25) }
            ]
        rd=datetime.datetime(2024,5,27)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)

#|

    #@unittest.SkipTest
    def testNextExps1(self):
        #stests = [ ]
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,21)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            


    #@unittest.SkipTest
    def testNextExps2(self):
        #stests = [ ]
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,22)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)

    #@unittest.SkipTest
    def testNextExps3(self):
        #stests = [ ]
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,23)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            

    #@unittest.SkipTest
    def testNextExps4(self):
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,24)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)            

    #@unittest.SkipTest
    def testNextExps5(self):
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,5,26) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,25)
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)

    #@unittest.SkipTest
    def testNextExps6(self):
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,6,2) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,5,27) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,5,28) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,5,29) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,5,30) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,5,31) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,1) }
            ]
        rd=datetime.datetime(2024,5,26) # sunday
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)
            
            
    #@unittest.SkipTest
    def testNextExps7(self):
        #skip_tests = [ ]
        tests = [
                  { "exp": "next sunday", "expected": datetime.datetime(2024,6,2) },
                  { "exp": "next monday", "expected": datetime.datetime(2024,6,3) },
                  { "exp": "next tuesday", "expected": datetime.datetime(2024,6,4) },
                  { "exp": "next wednesday", "expected": datetime.datetime(2024,6,5) },
                  { "exp": "next thursday", "expected": datetime.datetime(2024,6,6) },
                  { "exp": "next friday", "expected": datetime.datetime(2024,6,7) },
                  { "exp": "next saturday", "expected": datetime.datetime(2024,6,8) }
            ]
        rd=datetime.datetime(2024,5,27) # monday
        for t in tests:
            expstr=t["exp"]
            expected=t["expected"]
            self.dotest(expstr, rd, expected)


    #@unittest.SkipTest
    def testNextExps(self):
        tests = [ "next sunday", "next monday", "next tuesday", "next wednesday", "next thursday", "next friday", "next saturday" ]
        for t in tests:
            self.dotest(t)            

    #@unittest.SkipTest
    def testThisExps(self):
        tests = [ "this sunday", "this monday", "this tuesday", "this wednesday", "this thursday", "this friday", "this saturday" ]
        for t in tests:
            self.dotest(t)

    #@unittest.SkipTest
    def testArrowExpression(self):
        tests = [ "3 days ago", "in 3 days" ]
        for t in tests:
            self.dotest(t)
            
    #@unittest.SkipTest
    def testMonthExps(self):
        tests = [ "beginning of month", "end of month" ]
        for t in tests:
            self.dotest(t)

    #@unittest.SkipTest
    def testRelMonthExps(self):
        rd=datetime.datetime(2024,5,27)
        tests = [ "beginning of month", "end of month" ]
        for t in tests:
            self.dotest(t, rd)

    #@unittest.SkipTest
    def testNow(self):
        tests = [ "now", "today", "yesterday", "tomorrow" ]
        for t in tests:
            self.dotest(t)
            
    @unittest.SkipTest
    def testCompactExps(self):
        # TODO: These compact expressions do not work. Consider creating a translation mapping to valid arrow expressions
        week_tests = [ "1w", "-2w" ]
        #skip_tests = [ ]
        other_tests = [ "-2d", "+1m", "-7d",  "-2y",  "-2h", "+2h" ]
        for t in other_tests:
            self.dotest(t)
        for t in week_tests:
            self.dotest(t)            

if __name__ == "__main__":
    unittest.main()


now = arrow.now()
print( now.dehumanize("7 days ago") )

