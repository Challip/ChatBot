#improting modules fir bag of words
#######################################################
from nltk.tokenize import word_tokenize

import numpy as np
import string
import pandas as pd

userAsk="type of crypto"
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
def BagOfWord(userAsk):
    #read questions and ansers.cvs file
    QA=pd.read_csv("../Assessment_AI_2022/AI - assessment -Q&A.csv")
    QAdf=pd.DataFrame(QA)
    print(userAsk)
    #list of question
    questions=QAdf.iloc[:,0].tolist()
    #add user input to question list
    questions.append(userAsk)
    
    #implement bag of word algorith with CountVectorizer() method
    CountVec = CountVectorizer(ngram_range=(1,1),stop_words='english')
    Count_data = CountVec.fit_transform(questions)
    #Datafram of BoW (for cheacking)
    cv_df=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())

    ##################################################
    
    #implement Tf/idf with TfidfVectorizer()method
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(use_idf=True,smooth_idf=True,ngram_range=(1,1),stop_words='english')
    tfIdf_data = vectorizer.fit_transform(questions)
     
    #tfIdfData_df=pd.DataFrame(tfIdf_data.toarray(),columns=vectorizer.get_feature_names())


    feature_names=sorted(vectorizer.get_feature_names())
    docList=['Q01','Q02','Q03','Q04','Q05','Q06','Q07','Q08','Q09','Q10','Q11','Q12','User input']
    #Datafram of TF (for cheacking)
    skDocsTfIdfdf1 = pd.DataFrame(tfIdf_data.todense(),index=sorted(docList),  columns=feature_names)

    ###################################################
    #perform cosin_similarlity
    from sklearn.metrics.pairwise import cosine_similarity

    csim_tf = cosine_similarity(tfIdf_data,tfIdf_data)
    csim_tf_df = pd.DataFrame(csim_tf,index=sorted(docList),columns=sorted(docList))
    csim_BOW = cosine_similarity(Count_data,Count_data)
    csim_BOW_df = pd.DataFrame(csim_BOW,index=sorted(docList),columns=sorted(docList))
    ##################################################################
    
    tf=csim_tf_df[['User input']]
    #drop 0 and 1
    tf.drop(tf[tf['User input']<=0].index, inplace=True)
    #tf.drop(tf[tf['User input']>=1].index, inplace=True)
    tf.drop(tf.tail(1).index,inplace=True)
    m_tf=tf.idxmax()
    minstr=m_tf.to_string()
  
    BOW=csim_BOW_df[['User input']]

    BOW.drop(BOW[BOW['User input']<=0].index, inplace=True)
    #BOW.drop(BOW[BOW['User input']>=1].index, inplace=True)
    BOW.drop(BOW.tail(1).index,inplace=True)
    m_bow=BOW.idxmax()
    minstr2=m_bow.to_string()
    #print("Tfid= "+minstr2 )
    
    #compare cosin_similarlity result of Bow and Tf/idf -> if result of Bow and Tf are equal -> print the correct answer
    if minstr==minstr2:
        # select answer
        if minstr=="User input    Q01":
            answerText=QAdf['Answers'].iloc[0]
        elif minstr=="User input    Q02":
            answerText=QAdf['Answers'].iloc[1]
        elif minstr=="User input    Q03":
            answerText=QAdf['Answers'].iloc[2]
        elif minstr=="User input    Q04":
            answerText=QAdf['Answers'].iloc[3]
        elif minstr=="User input    Q05":
            answerText=QAdf['Answers'].iloc[4]
        elif minstr=="User input    Q06":
            answerText=QAdf['Answers'].iloc[5]
        elif minstr=="User input    Q07":
            answerText=QAdf['Answers'].iloc[6]
        elif minstr=="User input    Q08":
            answerText=QAdf['Answers'].iloc[7]
        elif minstr=="User input    Q09":
            answerText=QAdf['Answers'].iloc[8]
        elif minstr=="User input    Q10":
            answerText=QAdf['Answers'].iloc[9]
        elif minstr=="User input    Q11":
            answerText=QAdf['Answers'].iloc[10]
        elif minstr=="User input    Q12":
            answerText=QAdf['Answers'].iloc[11]
    #result of BoW and Tf/idf not match:
    elif minstr !=minstr2:
        print ("No match! try again")
        
    #print (answerText)
    return answerText
    #print (answerText)

 
    #return (answer)




BagOfWord("type of crypto")
#import sys
#print (sys.path)

