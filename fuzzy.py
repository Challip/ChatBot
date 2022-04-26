
from simpful import *

# Create a fuzzy system object
FS = FuzzySystem()

# Define Price differnece fuzzy sets and linguistic variables
S_1 = FuzzySet(function=Triangular_MF(a=(-10), b=(-10), c=0), term="down")
S_2 = FuzzySet(function=Triangular_MF(a=(-5), b=0, c=5), term="stable")
S_3 = FuzzySet(function=Triangular_MF(a=0, b=10, c=10) , term="up")
FS.add_linguistic_variable("Price", LinguisticVariable([S_1, S_2, S_3], concept="Price difference", universe_of_discourse=[-10,10]))


# Define Amount fuzzy sets and linguistic variable
T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small")
T_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=10), term="big")
FS.add_linguistic_variable("Amount", LinguisticVariable([T_1,T_2],concept="amount of coin",universe_of_discourse=[0,10]))

# Define output fuzzy sets and linguistic variable
F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="low")
F_2 = FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="medium")#F_3 = FuzzySet(function=Trapezoidal_MF(a=5, b=10, c=15, d=15), term="high")
F_3 = FuzzySet(function=Trapezoidal_MF(a=5, b=10, c=15, d=15), term="high")
FS.add_linguistic_variable("risk", LinguisticVariable([F_1, F_2,F_3], universe_of_discourse=[0,15]))

# Define fuzzy rules
R1 = "IF (Price IS down) OR (Amount IS big) THEN (risk IS high)"
R2 = "IF (Price IS stable) THEN (risk IS medium)"
R3 = "IF (Price IS up) OR (Amount IS small) THEN (risk IS low)"
FS.add_rules([R1, R2, R3])


# Perform Mamdani inference and print output
#print(FS.Mamdani_inference(["risk"]))

#FS.produce_figure()

def risk(amount,tprice,yprice):
    #convert input into int
    amount=int(amount)
    tprice=int(tprice)
    yprice=int(yprice)
    #check the input
    #today price and yesterday price can not be > 10
    if (tprice >10) or (tprice<0) or (yprice >10) or (yprice<0) :
        print (" Please enter the price with positive scientific notation coefficient (less than 10)")
        
    else:
        if (amount >10) or (amount <0 ):
            print ("Maximum coin amount is 10!")
        else:
            #find price difference 
            inputprice=tprice-yprice
            amount=amount
            # Set antecedents values
            FS.set_variable("Price", inputprice)
            FS.set_variable("Amount",amount)
    
            # Perform Mamdani inference and print output
            riskP=(FS.Mamdani_inference(["risk"]))
            print (riskP)
            #covert risfP dict into float
            riskNum=(riskP["risk"])
            if (riskNum >=0 and riskNum <5):
                print("risk is Low")
            elif (riskNum >=5 and riskNum <10):
                print("risk is medium")
            elif (riskNum > 10):
                print ("risk is high")

    

        
#risk(10,2,9)
    