#!/usr/bin/python
import survey
# print number of pregancies
# counts the number of live births
# partition the live birth records into two groups,one for first babies and one for the others
# compute the average pregnancy length for first babies and others.
def MakeTable(data_dir=''):

def Summarize(data_dir):
    table = survey.Pregnancies()
    table.ReadRecords()
    print 'Number of pregnancies', len(table.records)



def main(name,data_dir='.'):
    Summarize(data_dir)

if __name__ == '__main__':
    import sys
    main(*sys.argv) # take sys.argc and upwrap this list into the rest of parameters of main
