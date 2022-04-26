from nltk.sem import Expression
from nltk.inference import ResolutionProver
from nltk.sem import Valuation, Model
import pandas as pd
import csv

FOL_file="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/FOL.csv"
fol=pd.read_csv(FOL_file)
#print (fol)
read_expr=Expression.fromstring

p2=read_expr("worthM (BTC,y) &token (y)")
p5=read_expr("worthM (x2,y2) & coin (x2) -> privacy(y2)")
p8=read_expr("stablecoin (USDT)")
p9=read_expr("token (ONE)")
p1=read_expr("coin (BTC)")
p7=read_expr("fiat (f) -> -stablecoin(f)")
p20=read_expr("fiat (x) -> worthM(x,y) & stablecoin (y)")
p21=read_expr("fiat(USD)")
p22=read_expr("buy (b,z) & stablecoin (b) -> token(z)")
#p9=read_expr("token (ONE) -> -coin (ONE) | - privacy (ONE) | -stablecoin (ONE)")
kb=[p1,p2,p9,p20,p8]
#kb=[p7,p8]

q=read_expr('worthM(ONE,BTC)')
prove=ResolutionProver().prove(q,kb,verbose=True)
print(prove)




q1=read_expr("coin (c) -> - token (c)")
q2=read_expr("token (t) -> -stablecoin (t)")
q3=read_expr("stablecoin (s) -> - privacy (s)")
q4=read_expr('privacy (p) -> -coin(p)')
q5=read_expr('stablecoin (ONE)')

qqq=[q1,q2,q3,q4,q5]
q=read_expr('token (ONE)')
prove=ResolutionProver().prove(q,qqq,verbose=True)
print(prove)

 
p=["Mars"]
s=[]
ip="Earth"
l=""
if ip in p:
    q=read_expr('star ('+ ip+')')
    prove=ResolutionProver().prove(q,qqq,verbose=True)
    print(prove)
    if prove==False:
        print (" not by the rule")
    elif prove ==True:
        print ("Correct")
elif ip not in p:
    q=read_expr("planet (" +ip+") -> -star(" +ip+")")
    print(prove)
    if prove== True:
        p.append(ip)
        qqq.append(q)
        print("I will remember that")
    elif prove==False:
        print ("Sth wrong")
else:
    print ("Catch error")
    
        





read_expr=Expression.fromstring

FOL_file_OUT="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/FOL_OUT.csv"
FOL_file="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/FOL.csv"
fol=pd.read_csv(FOL_file_OUT)
#print (fol)
#FOL list
kb=[]
for ind in fol.index:
    fa=(fol["FOL"][ind])
    p=read_expr(fa)
    kb.append(p)
       
#print(kb[-6:])
tt=kb[:7]
#tt=kb
print(tt)

yy=kb[-7:]
    
qq=read_expr("stablecoin (USDT)")
yy.append(qq)
print(yy)
what=read_expr(" worthM(USDT,BTC)")
prover=ResolutionProver().prove(what,yy,verbose=True)
print(prover)





print (yy)




read_expr=Expression.fromstring
ctype=""
ipc=""
clist=["BTC","USD","USDT"]

    ###############################################################
def prove_logic(star1,star2,tt,clist):
    star2=(star2.lower())
    star1=(star1.upper())
    #print (star2)
    if star2=="payment currency":
        #ctype=("coin (" + star1 +") -> -token (" + star1 + ") | - privacy (" + star1+") | -stablecoin (" + star1+ ')')
        ipc=("coin (" + star1 + ")")
        #clist=coin_list
    elif star2=="privacy coin":
        #ctype=("privacy (" + star1 +") -> -token (" + star1 + ") | - coin (" + star1+") | -stablecoin (" + star1+ ')')
        ipc=("privacy (" + star1 + ")")
        #clist=privacy_list
    elif star2 =="utility token":
        #ctype=("token (" + star1 +") -> -coin (" + star1 + ") | - privacy (" + star1+") | -stablecoin (" + star1+ ')')
        ipc=("token (" + star1 + ")")
        #clist=token_list
    elif star2=="stablecoin":
        #ctype=("stablecoin (" + star1 +") -> -token (" + star1 + ") | - privacy (" + star1+") | -coin (" + star1+ ')')
        ipc=("stablecoin (" + star1 + ")")
        #clist=stable_list
    else:
        print ("undefind")
    
   
    uip=(ctype)
    print (uip)
    print ("This is ipc: " +ipc)
    print (star1)
    print (clist)
    
    #qq=read_expr()
    #prover=ResolutionProver().prove(qq,tt,verbose=True)
    
    if star1 in clist:
        qq=read_expr(ipc)
        prover=ResolutionProver().prove(qq,tt,verbose=True)
        print(prover)
        if prover==False:
            print ("Sorry this contradict with what I know! ")
        elif prover ==True:
            print ("Correct")
    elif star1 not in clist:
        #qq=read_expr(ctype)
        #prover=ResolutionProver().prove(qq,tt,verbose=True)
        #print(prover)
        #if prover== True:
        try:
            q=read_expr(ipc)
            clist.append(star1)
            tt.append(q)
            yy.append(q)
            print("OK, I will remember that "+ star1 +" is " + star2 )
        #elif prover==False:
        except:
            print ("Sth wrong")
    else:
        print ("Catch error")    
    
    #return clist
    #return tt


def worthmore (s1,s2,tt):
    s1=(s1.upper())
    s2=(s2.upper())
    ip=("worthM(" + s1 +"," +s2+")")
    qq=read_expr(ip)
    prover=ResolutionProver().prove(qq,tt,verbose=True)
    if prover ==True:
        print ("Yes, " +s1+" worth more than " +s2)
    elif prover ==False:
        print ("No, " +s1+" worth less than " +s2)

    
qq=read_expr("coin (tw)")
prover=ResolutionProver().prove(qq,tt,verbose=True)
print(prover)
prove_logic("tw","stablecoin",tt,clist)
print (tt)
c= (prove_logic("tw","stablecoin",tt,clist))
print (c)
##############################################################
import aiml
# Create a Kernel object. No string encoding (all I/O is unicode)
kern = aiml.Kernel()
kern.setTextEncoding(None)
# Use the Kernel's bootstrap() method to initialize the Kernel. The
# optional learnFiles argument is a file (or list of files) to load.
# The optional commands argument is a command (or list of commands)
# to run after the files are loaded.
# The optional brainFile argument specifies a brain file to load.
kern.bootstrap(learnFiles="C:/Users/i_am-/.spyder-py3/Assessment_AI_2022/out.xml")

######################################################
#improting modules fir bag of words
#######################################################

# Welcome user
#######################################################
print("Welcome to this chat bot. Please feel free to ask questions from me!")
#######################################################
# Main loop
#######################################################
while True:
    #get user input
    try:
        userInput = input("> ")
    except (KeyboardInterrupt, EOFError) as e:
        print("Bye!")
        break
    #pre-process user input and determine response agent (if needed)
    responseAgent = 'aiml'
    clist=clist
    tt=tt
    #activate selected response agent
    if responseAgent == 'aiml':
        #userInput=BagOfWord(userInput)
        answer = kern.respond(userInput)
    #post-process the answer for commands
    if answer[0] == '#':
        params = answer[1:].split('$')
        cmd = int(params[0])
        if cmd == 0:
            print(params[1])
            break
        elif cmd == 1:
            
            
            try:
                prove_logic(params[1], params[2], tt, clist)
                  
            except:
                print("Sorry, I do not know that")
        elif cmd==2:
            try:
                worthmore(params[1],params[2],tt)
            except:
                print ("Sorry, I dont know that")
        elif cmd == 99:
            print("I did not get that, please try again.")
    
    else:
    
        print(answer)
        
        
##################################################################
# Implementing bag of words
###########################################