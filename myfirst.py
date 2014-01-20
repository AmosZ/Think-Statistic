#!/usr/bin/python
import survey
import statistic
import myPmf
# print number of pregancies
# counts the number of live births
# partition the live birth records into two groups,one for first babies and one for the others
# compute the average pregnancy length for first babies and others.

def PartitionTable(table):
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for rec in table.records:
        if rec.outcome != 1:
            continue
        else:
            if rec.birthord == 1:
                firsts.AddRecord(rec)
            else:
                others.AddRecord(rec)
    return firsts,others

def MakeTable(data_dir):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    firsts,others = PartitionTable(table)

    return firsts,others,table

def ProcessTables(*tables):
    for table in tables:
        Process(table)

def Process(table):
    table.length = [rec.prglength for rec in table.records]
    table.n = len(table.length)
    table.mu = Mean(table.length)
    table.var = statistic.Variance(table.length,table.mu)
    table.stdvar = statistic.StandardVar(table.length,table.mu)
    
def Mean(n):
    return float(sum(n))/len(n)


def Summarize(data_dir='.'):
    firsts,others,table = MakeTable(data_dir)
    ProcessTables(firsts,others)
    
    print 'Number of Pregnancies :',len(table.records)
    print 'Number of first babies:',firsts.n
    print 'Number of other babies:',others.n
    print ''
    print 'Mean weeks of first baby:',firsts.mu
    print 'Mean week of other baby:',others.mu
    print 'Variance of first baby:',firsts.var
    print 'Variance of other baby:',others.var
    print 'Standard Variance of first baby:',firsts.stdvar
    print 'Standard Variance of other baby:',others.stdvar
    print ''
    print 'Difference in hours : ',(firsts.mu - others.mu)* 7.0 *24.0

    first_pmf = myPmf.MakePmfFromList(firsts.length)
    other_pmf = myPmf.MakePmfFromList(others.length)

    first_pmf.Normalize()
    other_pmf.Normalize()

    first_pmf.Plot()
def main(name,data_dir='.'):
    Summarize(data_dir);    #function in summary

if __name__ == '__main__':
    import sys
    main(*sys.argv)
