from nltk.sem import Expression
from nltk.inference import ResolutionProver
from nltk.sem import Valuation, Model
import pandas as pd
import csv
              
  

read_expr=Expression.fromstring

FOL_file_OUT="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/FOL_try.csv"
fol=pd.read_csv(FOL_file_OUT)
#print (fol)
#FOL list
kb=[]
for ind in fol.index:
    fa=(fol["FOL"][ind])
    p=read_expr(fa)
    kb.append(p)
       


print(kb)







what=read_expr(" fiat (ONE)")
prover=ResolutionProver().prove(what,kb,verbose=True)
print(prover)