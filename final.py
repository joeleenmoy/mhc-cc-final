# mhc-cc-final
#jason woo, hanna yoo and joeleen moy

import random
import time 
import sys

global orig

    
def wordcount(filename):
    """
        Simple Word counter that returns
        the length of the file it is reading.
    """
    f = open( filename )
    text = f.read()
    f.close()

    LoW = text.split()    
    count = len(LoW)
    return count

def mk(filename):
    """
        mk for Markov, this function exports a 
        dictionary with the words from the text file.
        It formats the text for the next function. 
    """
    global orig
    f = open( filename )
    text = f.read()
    f.close()

    LoW = text.split()    
    orig = LoW[:]

    d = {}
    ow = "$"
    
    for nw in LoW:
        if "." in ow or "?" in ow or "!" in ow:
            d["$"] += [nw]
        elif ow not in d:
            d[ow] = [ nw ]
        else:
            d[ow] += [ nw ]
        ow = nw
    return d  

def generateText(d,n):
    """
        This function generates text by taking
        random words from the dictionary (above)
        and arranging them in a new order.
    """
    ow = "$"
    counter = 0

    while n > 0:
        if ow not in d:
            ow = '$'
        nw = random.choice( d[ow] )

        print nw,
        sys.stdout.flush()
        counter += 1
        if counter%10 == 0: print

        ow = nw

        n -= 1
        time.sleep(random.choice([.1,.2,.3,.4]))

def randomText(d,n):
    """
        Essentially the same as 'generateText'
        excpet the letters of the words chosen 
        are randomized.
    """
    ow = "$"
    counter = 0

    while n > 0:
        if ow not in d:
            ow = '$'
        nw = random.choice( d[ow] )
        rw = ''.join(random.sample(nw,len(nw)))

        print rw,
        sys.stdout.flush()
        counter += 1
        if counter%10 == 0: print
        ow = nw

        n -= 1
        time.sleep(random.choice([.1,.2,.3,.4]))

def final():
    """
        final lets the user choose a text final
        then outputs a short portion of it. 
        1. Portion of the original text
        2. Portion from Markov process
        3. Words from Markov with randomized letters 
    """
    global orig
    x = raw_input("What is the name of the txt file that you want to use? \n")
    "\n"
    count = wordcount(x)
    print "There are", count, "words in the file."
    

    print "\n"
    print "----------------------------------------------------------------------"
    
    d = mk(x)
    
    counter = 0
    for i in orig[:76]:
        print i,
        sys.stdout.flush()
        counter += 1
        if counter%10 == 0: print
        time.sleep(random.choice([.1,.2,.3,.4]))

    print "\n"

    generateText(d,(.004*count))
    
    print "\n"
    
    randomText(d,(.004*count))
