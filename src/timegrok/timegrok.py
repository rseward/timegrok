#!/usr/bin/env python

from enum import Enum
import datetime
import spacy
import re
from word2number import w2n
from icecream import ic

class TimeUnit(Enum):
    SECOND = 1
    MINUTE = 60
    HOUR = 60*60
    DAY = 24*60*60
    WEEK = 7*24*60*60
    MONTH = int(365*24*60*60/12)
    YEAR = 365*24*60*60


class TimeInterpreter(object):
    """
    Class to interpret common human time expressions (often temporal time references) into concrete absolute datetime objects.
    Note the focus of the class is for short term future time expressions. E.g. time strings a user of a personal voice assistant
    would use to set reminders.

    from timegrok.timegrok import TimeInterpreter

    tgrok = TimeInterpreter()
    t1=tgrok.grok("in twenty minutes")
    """
    
    def __init__(self):
        self.secre = re.compile( r'(.*) (second)s?')        
        self.minre = re.compile( r'(.*) (minute)s?')
        self.hourre = re.compile( r'(.*) (hour)s?')
        self.dayre = re.compile( r'(.*) (day)s?')
        self.weekre = re.compile( r'(.*) (week)s?')        
        self.monthre = re.compile( r'(.*) (month)s?')
        self.yearre = re.compile( r'(.*) (year)s?')
        self.timere = re.compile( r'(\d+):(\d\d)\s?(am|pm)?')
        self.nlp = spacy.load("en_core_web_sm")

    def grok(self, timestr, curtime=None, expectFuture=True):
        if curtime is None:
            curtime = datetime.datetime.now()

        tquantity=1 # Assume a quantity of one, should enable a use case like "In a minute"
        tunit=None
        esttime=None

        timeent = None
        doc = self.nlp(timestr)
        for ent in doc.ents:
            #help(ent)
            print(ent.label_, ent)
            if ent.label_ in  ["TIME","DATE"]:
                timeent = ent.text
                #print(ent.label_, ent.text)
            
        if timeent is not None:
            #print("Extracting time.")
            if "at" in timestr.lower():
                m = self.timere.match(timeent)
                if m:
                    esttime = self.interpretTimeMatch( m, curtime, expectFuture)
                else:
                    esttime = self.interpretTimeWord( timeent, curtime, expectFuture)
            else:                  
                for token in self.nlp(timeent):
                    if token.like_num:
                        tquantity=self.getinteger(token.text)
                        #print(tquantity)

                tunit = self.gettimeunit(timeent.lower())

        # Do the relative time calculation
        print ( f"{tquantity=} , {tunit=}" )
        if tquantity is not None and tunit is not None:
            secstoadd = tquantity * tunit.value

            esttime = curtime + datetime.timedelta(seconds=secstoadd)

        return esttime

    def trytomorrow(self, curtime, hh, mm):
        tomorrow=curtime + datetime.timedelta(1)
        ptime = datetime.datetime( tomorrow.year, tomorrow.month, tomorrow.day, hh, mm)
        return ptime

    def trytoday(self, curtime, hh, mm):
        ptime=datetime.datetime( curtime.year, curtime.month, curtime.day, hh, mm)
        return ptime
        

    def interpretTimeMatch(self, tm, curtime, expectFuture):
        hh=int(tm.group(1))
        mm=int(tm.group(2))
        ampm=None
        if tm.group(3):
            ampm=tm.group(3)
        if ampm is not None and ampm == "pm":
            hh=hh+12
            
        ptime = self.trytoday(curtime, hh, mm)
        if expectFuture:
            if ptime > curtime:
                return ptime
            else:
                return self.trytomorrow( curtime, hh, mm )

        return None

    def interpretTimeWord(self, timestr, curtime, expectFuture):
        ic( f"{timestr=}, {curtime=}, {expectFuture=}" )
        hh=None
        mm=None
        if "noon" in timestr:
            (hh,mm)=(12,00)
        if "midnight" in timestr:
            (hh,mm)=(00,00)
        if "dawn" in timestr:
            (hh,mm)=(6,00)
        if "evening" in timestr:
            (hh,mm)=(18,00)
        if "night" in timestr:
            (hh,mm)=(21,00)

        ic( f"{hh=} {mm=}" )

        if hh is not None and mm is not None and expectFuture:
            ptime = self.trytoday(curtime, hh, mm)
            if ptime > curtime:
                return ptime
            else:
                return self.trytomorrow( curtime, hh, mm )

        return None
        

    def getinteger(self, qstr):
        ret=None
        try:
            ret=int(qstr)
        except:
            try:
                #print( f"word2number({qstr})" )
                ret = w2n.word_to_num(qstr)
            except:
                raise

        return ret

    def gettimeunit(self, timestr):
        ret=None
        if self.minre.match(timestr):
            ret=TimeUnit.MINUTE
        elif self.hourre.match(timestr):
            ret=TimeUnit.HOUR
        elif self.dayre.match(timestr):
            ret=TimeUnit.DAY
        elif self.weekre.match(timestr):
            ret=TimeUnit.WEEK
        elif self.monthre.match(timestr):
            ret=TimeUnit.MONTH            
        elif self.yearre.match(timestr):
            ret=TimeUnit.YEAR
        elif self.secre.match(timestr):
            ret=TimeUnit.SECOND

        return ret

if __name__ == "__main__":
    import sys
    tgrok = TimeInterpreter()

    # Quick cli tester
    print(tgrok.grok(sys.argv[1]))

    
