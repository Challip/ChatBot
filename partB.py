
from nltk.sem import Expression
from nltk.inference import ResolutionProver
from nltk.sem import Valuation, Model
import pandas as pd
import csv



#read_expr=Expression.fromstring
#read logic file
FOL_file_OUT="../Assessment_AI_2022/FOL_OUT.csv"
fol=pd.read_csv(FOL_file_OUT)

#ntlk expression
read_expr=Expression.fromstring

#load logic in to list
kb=[]
for ind in fol.index:
    fa=(fol["FOL"][ind])
    p=read_expr(fa)
    kb.append(p)

#logic list
tt=kb[:8]
yy=(kb[-7:])
print(yy)
qq=read_expr("worthM(USDT,BTC)")
#prove userinput with FOl logic
prover=ResolutionProver().prove(qq,yy,verbose=False)
print(prover)
#list of coin that already in Logic
clist=["BTC","USD","USDT"]

    ###############################################################
def prove_logic(star1,star2,tt,clist):
    star2=(star2.lower())
    star1=(star1.upper())
    
    #convert userinput to proper syntex for prover
    read_expr=Expression.fromstring
    if star2=="payment currency":
        ipc=("coin (" + star1 + ")")
    elif star2=="privacy coin":
        ipc=("privacy (" + star1 + ")")
    elif star2 =="utility token":
        ipc=("token (" + star1 + ")")
    elif star2=="stablecoin":
        ipc=("stablecoin (" + star1 + ")")
    else:
        print ("undefind")
        

    #if the coin is already declared prove the statment 
    if star1 in clist:
        qq=read_expr(ipc)
        #prove userinput with FOl logic
        prover=ResolutionProver().prove(qq,tt,verbose=False)
        print(prover)
        if prover==False:
            print ("Sorry this contradict with what I know! ")
        elif prover ==True:
            print ("Correct")
            
            
    #if the coin is not  declared ->prove the statment -> 
    #if true , add the coin to coin list and add new logic to logic list
    elif star1 not in clist:
        try:
            q=read_expr(ipc)
            clist.append(star1)
            tt.append(q)
            yy.append(q)
            print("OK, I will remember that "+ star1 +" is " + star2 )
        except:
            print ("Sth wrong")
    else:
        print ("Catch error")    
        
    ######################################################################
#class for prove worth more statement
def worthmore (s1,s2,yy):
    
    read_expr=Expression.fromstring
    s1=(s1.upper())
    s2=(s2.upper())
    #prepare correct syntex
    ip=("worthM(" + s1 +"," +s2+")")
    qq=read_expr(ip)
    prover=ResolutionProver().prove(qq,yy,verbose=False)
    if prover ==True:
        print ("Yes, " +s1+" worth more than " +s2)
    elif prover ==False:
        print ("No, " +s1+" worth less than " +s2)


