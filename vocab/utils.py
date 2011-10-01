"""
Yule's I measurement courtesy of Swizec Teller, 
http://swizec.com/blog/measuring-vocabulary-richness-with-python/swizec/2528
"""

from nltk.stem.porter import PorterStemmer
from itertools import groupby
 
def words(entry):
    return filter(lambda w: len(w) > 0,
                  [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])
 
def yule(entry):
    # yule's I measure (the inverse of yule's K measure)
    # higher number is higher diversity - richer vocabulary
    d = {}
    stemmer = PorterStemmer()
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
 
    M1 = float(len(d))
    M2 = sum([len(list(g))*(freq**2) for freq,g in groupby(sorted(d.values()))])
 
    try:
        return (M1*M1)/(M2-M1)
    except ZeroDivisionError:
        return 0