import sys
def TRUEORFALSE():
    answer = str(input("")).lower()
    if(answer == "yes"):
        result = True
    else: 
        result = False
    return result

def COUGH():
    print("Are you coughing?")
    return TRUEORFALSE()

def BREATH():
    print("Are you short of breath or wheezing or coughing up phlegm?")
    return TRUEORFALSE()

def HEADACHE():
    print("Do you have a headache?")
    return TRUEORFALSE()

def ACHING():
    print("Do you have aching bones or aching joints?")
    return TRUEORFALSE()

def RASH():
    print("Do you have a rash?")
    return TRUEORFALSE()

def THROAT():
    print("Do you have a sore throat?")
    return TRUEORFALSE()

def KIDNEY():
    print("Do you have a back pain just above the waist with chills and fever?")
    return TRUEORFALSE()

def UNINARY():
    print("Do you have pain urinating more often?")
    return TRUEORFALSE()

def HEAT():
    print("Have you spent the day in the sun or in hot conditions?")
    return TRUEORFALSE()

def MENIGITIS():
    print("Are you experiencing any of the following: pain when bending your head forward, nausea or vomiting, bright light hurting your eyes, drowsiness or confusion?")
    return TRUEORFALSE()

def DIGESTIVE():
    print("Are you vomiting or had diarrhea?")
    return TRUEORFALSE()

if (COUGH()):
    if(BREATH()):
        print("Possibilites include pneumonia or infection of airways")
        sys.exit()
if(HEADACHE()):
    if(MENIGITIS()):
        print("Possibilities include menigitis")
        sys.exit()
    if(DIGESTIVE()):
        print("Possibilities include digestive tract infection")
    else:
        print("Possibilities include viral infection")
else:
    if(ACHING()):
        print("Possibilities include viral infection")
    else:
        if(RASH()):
            print("Insufficient information to list possibilities")
        else:
            if(THROAT()):
                print("Possibilities include a throat infection")
            else:
                if(KIDNEY()):
                    print("Possibilities include kidney infection")
                else:
                    if(UNINARY()):
                        print("Possibilities include a urinary tract infection")
                    else:
                        if(HEAT()):
                            print("Possibilities include sunstroke or heat exhaustion")
                        else:
                            print("Insufficient information to list possibilities")