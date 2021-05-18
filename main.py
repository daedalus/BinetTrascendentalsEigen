#!/usr/bin/env python3
# Author Dario Clavijo 2021

"""
This program finds in the OEIS, series of numbers produced by the binet formula with a combination of trascendental numbers.
It is not intended to bruteforce the OEIS database but to find new relations in the existing formulas.
"""

import oeispy as op
import math
import sys

tras = [math.e, math.pi]
tras += [math.e ** math.pi, math.pi ** math.e]
tras += [math.pi ** math.sqrt(2), math.e ** math.sqrt(2), math.sqrt(2)**math.pi, math.sqrt(2)**math.e]
tras += [math.sqrt(5) * math.sqrt(2), math.sqrt(5)**math.sqrt(2), math.sqrt(2) ** math.sqrt(5), math.sqrt(5) ** math.sqrt(5), math.sqrt(2) ** math.sqrt(2)]
tras += [2*math.sqrt(2), 1 + math.sqrt(2), 1 - math.sqrt(2), 1 + math.sqrt(5), math.sqrt(5), 1 - math.sqrt(5), (1+math.sqrt(5))/2 , (1-math.sqrt(5))/2]
tras += [math.cos(1),math.sin(1),math.tan(1)] 


def binet(a,b,n):
    #print(a,b,n)
    return round((pow(a,n) - pow(b,n))/(a-b))


def gen_serie(a,b,l):
  tmp = []
  for c in range(0,l):
     tmp.append(str(binet(a,b,c)))
  s = ",".join(tmp)
  return s


def gen_series(l):
    for a in range(0,l):
        for b in range(a,l):
            if a != b:
                s = gen_serie(a,b,l)
                #res = op.resultEois(s)
                res = op.resultEois(s.replace("0,1,",""))
                #except:
                #    res = None
                if res != None:
                    name = op.getName(res[0])
                    number = op.getNumber(res[0])
                    S = "%d, %d, A%06d, %s\n" % (a,b,number,name)
                    sys.stderr.write(S)
                    sys.stdout.write(S)
                    sys.stdout.flush()
                    sys.stderr.flush()


def gen_series_tras(l):
    series = []
    lt = len(tras)
    for i in range(0,lt):
        a = tras[i]
        for j in range(i,lt):
            b = tras[j]
            if a != b:
                series.append((i,j,0,gen_serie(a,b,l)))  
                series.append((i,j,1,gen_serie(a*b,a,l)))
                series.append((i,j,2,gen_serie(a*b,b,l)))
                series.append((i,j,3,gen_serie(a*b,a/b,l)))
                series.append((i,j,4,gen_serie(a*b,b/a,l)))
                series.append((i,j,5,gen_serie(a+b,a-b,l)))

    for i,j,k,s in series:
        s = s.replace("0,1,","")
        sys.stderr.write("[%d %d %d] %s\n" % (i,j,k,s))
        res = op.resultEois(s)
        #except:
        #    res = None
        if res != None:
            name = op.getName(res[0])
            number = op.getNumber(res[0])
            S = "%d, %d, %d, A%06d, %s\n" % (i,j,k,number,name)
            sys.stderr.write(S)
            sys.stdout.write(S)
            sys.stdout.flush()
            sys.stderr.flush()


if __name__ == "__main__":
  #gen_series(10)
  gen_series_tras(int(sys.argv[1]))
