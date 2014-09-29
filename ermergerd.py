#!/usr/bin/python

import sys, re

def ermergerd(w):
    """
    I am aware nltk exists.
    ermergerd a werd
    replace y only if not at the beginning of a word
    replace e only if not at end of word
    if vowel sequence followed by 'r', do not put two r's, e.g. "word " --> "werd"


    cases not handled / handled incorrectly:
    * punctuation. lol.
    * "nlp is hard" > "nlp ers herrd" instead of "nlp ers herd"
    * irregular spelling like "brought"
    * "buying" > "bererin" for some reason.
    * "sequence" > "serqernc"
    * "say" "may" etc > "SERER" 
    
    Eventually turn this into a web app with flask. It is superior to J. Miller's app. At least on test cases like "penguins who are buying things"

    >>> economic demography
    ERCERNERMERC DERMERGRERPHER
    """
    w = w.strip().lower()
    derctshernerer = {'me':'meh','you':'u', 'are':'er', "you're":"yer", "i'm":"erm", "i've":"erv", "my":"mah", "the":"da", "omg":"ermahgerd"}
    if w in derctshernerer:
        return derctshernerer[w].upper()
    else:
        w = re.sub(r"[\.,/;:!@#$%^&*\?]+", '', w) # punctuation is hard. another day. 
        w = re.sub(r"tion", "shun", w)
        pat = r"[aeiouy]+"
        er =  re.sub(pat, "er", w)
        if w.startswith('y'):
            er = 'y' + re.sub(pat, "er", w[1:])
        if w.endswith('e') and not w.endswith('ee') and len(w)>3:
            er = re.sub(pat, "er", w[:-1]) 
        if w.endswith('ing'):
            er = re.sub(pat, "er", w[:-3]) + 'in'
        er = er[0] + er[1:].replace('y', 'er')
        er = er.replace('rr', 'r')
        return er.upper()

def trernslert(werds):
    terkerns = werds.split()
    er = ''
    for terk in terkerns:
        werd = ermergerd(terk)
        er = er + ' ' + werd
    return er

if __name__ == "__main__":
    try:
        s = sys.argv[1]
        print trernslert(s)
    except IndexError:
        print "Press Ctrl+c to exit\n"
        while(1):
            try:
                ernpert = raw_input("Whert der yer wernt ter trernslert?: ")
                print trernslert(ernpert) + "\n"
            except KeyboardInterrupt:
                print "\nGerdber"
                sys.exit()
            
