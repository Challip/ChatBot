
#######################################################
from nltk.tokenize import word_tokenize
import numpy as np
import string
import pandas as pd
from Bag_of_words import BagOfWord
from fuzzy import risk


#######################################################
# Initialise for partB (nltk)
#######################################################
from partB import prove_logic
from partB import worthmore
from nltk.sem import Expression
from nltk.inference import ResolutionProver
from nltk.sem import Valuation, Model
import pandas as pd
import csv
#read logic file
FOL_file_OUT="../Assessment_AI_2022/FOL_OUT.csv"
fol=pd.read_csv(FOL_file_OUT)
######################################
#initialise for partC
from predic import img_classi
from video_pred import video_class
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from PIL import Image
#####################################
#Part D
from translate import translate_text
from ImgClass_cloud import cloud_class
####################################

#ntlk expression
read_expr=Expression.fromstring

#load logic in to list
kb=[]
for ind in fol.index:
    fa=(fol["FOL"][ind])
    p=read_expr(fa)
    kb.append(p)
#logic list
#logic list
tt=kb[:8]
yy=(kb[-7:])
#list of coin that already in Logic
clist=["BTC","USD","USDT"]

#######################################################
# Initialise crypto price agent
#######################################################
from cryptoprice import get_crypto_price
import requests
import pandas as pd
import json, requests
from datetime import datetime
api_key = 'MRzAy2PbkeE5IkK7Ad1mHPTAUPQS7MvP'

#######################################################
#  Initialise AIML agent
#######################################################
import aiml
# Create a Kernel object. No string encoding (all I/O is unicode)
kern = aiml.Kernel()
kern.setTextEncoding(None)
kern.bootstrap(learnFiles="../Assessment_AI_2022/Assesstment_AI_2022.xml")

######################################################
#improting modules fir bag of words
#######################################################

# Welcome user
#######################################################
print("Welcome to cryptocurrecy chat bot. Please feel free to ask questions about basic cryptocurrecies!")
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

    if responseAgent == 'aiml':
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
        elif cmd == 2:
            try:
                worthmore(params[1],params[2],yy) 
            except:
                print("Sorry, I do not know that")
        elif cmd == 3:
            get_crypto_price(params[1], api_key)
        elif cmd == 4:
            risk(params[1], params[2], params[3])
        #Part C: image classification
        elif cmd == 5:
                fileName=askopenfilename()
                class_answer=img_classi(fileName)
                Cans=cloud_class(fileName)
                print (class_answer)
                print(Cans)
        #Part C: vedio classification
        elif cmd == 6:
            videoPath=askopenfilename()
            video_class(videoPath)
        elif cmd == 99:
            try:
                #if input don't match aiml -> perform Similarity base component
                Bag=BagOfWord(userInput)
                print (Bag)
                # Cloud translator
                print("Do you want to translate answer to German?")
                transInput = input(">> ")
                if transInput == "Yes":
                    text_to_translate = str(Bag)
                    translation = translate_text(text_to_translate)
                    print("Translate to German: " + translation)
                    continue
                elif transInput == "No":
                    print("Don't translate")
                    continue
            except:
                print("I did not get that, please try again.")            
    else:
        
        print(answer)
    

