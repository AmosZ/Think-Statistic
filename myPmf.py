#!/usr/bin/python
import math
class _DictWrapper(object):
    """An object that contain a directory"""
    def __init__(self,d=None,name=''):
        if d == None:
            d = {}  # an empty directory
        self.d = d
        self.name = name

    def GetDict(self):
        return self.d

    def Values(self):
        """Get an unsorted sequence of values
        key : value of data
        value : frequency or probability of data
        """
        return self.d.keys()

    def Items(self):
        """Get an unsort sequnce of (value,freq/prob)"""
        return self.d.items()

    def Render(self):
        return zip(*sorted(self.Items()))

    def Print(self):
        """Print the values and freq/prob in ascending order"""
        for value,freq in sorted(self.d.iteritems()):
            print value,freq

    def Set(self,x,y = 0):
        self.d[x] = y

    def Incre(self,x,term=1):
        self.d[x] = self.d.get(x,0) + term

    def Mult(self,x,factor):
        self.d[x] *= self.d.get(x,0) * factor

    def Remove(self,x):
        del self.d[x]

    def Total(self):
        """Return total of the frequencies/probabilities in the map"""
        return sum(self.d.itervalues())
    def MaxLike(self):
        return max(self.d.itervalues())

    def Plot(self):
        import matplotlib.pyplot as pyplot
        val,prob = self.Render()
        pyplot.bar(val,prob)
        pyplot.show()

class Hist(_DictWrapper):
    def Freq(self):
        return self.d.get(x)

    def Freqs(self):
        return self.d.values()

    def Mode(self):
        _max =  max(self.d.values())
        for k in self.d.iterkeys():
            if self.d[k] == _max:
                return k

def MakeHistFromList(l,name=''):
    hist = Hist(name=name)
    for x in l:
        hist.Incre(x)
    return hist

def MakeHistFromDict(d,name=''):
    return Hist(d,name)

class Pmf(_DictWrapper):
    """Represents a probability mass function.
    Values can be any hashable type; probabilities are floating-point.
    Pmfs are not necessarily normalized.
    """

    def Prob(self,x):
        return self.d.get(x)

    def Probs(self):
        return self.d.values()

    def Normalize(self,fraction=1.0):
       total = self.Total() 

       factor = float(fraction)/total
       for x in self.d:
           self.d[x] *= factor

    def Mean(self):
        mu = 0
        for x,p in self.d.iteritems():
            mu += x*p
        return mu

    def Var(self):
        var = 0;
        mu = self.Mean()
        for x,p in self.d.iteritems():
            var += p*(x-mu)**2

    def Print(self,x=None):
        if x is None:
            for x,p in self.d.iteritems():
                print x,p
        else:
            print self.d[x]

def MakePmfFromList(l,name=''):
    hist = MakeHistFromList(l,name)
    return MakePmfFromHist(hist)

def MakePmfFromDict(d,name=''):
    pmf = Pmf(d,name)
    pmf.Normalize()
    return pmf

def MakePmfFromHist(h,name=None):
   if name is None:
        name = h.name

   d = dict(h.GetDict())
   pmf = Pmf(d,name)
   pmf.Normalize()
   return pmf
