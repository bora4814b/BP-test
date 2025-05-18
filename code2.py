import pyttsx3
def speek(a):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    text = a
    engine.say(text)
    engine.runAndWait()
print("""enter your blood pressure level
      like:-120/80""")
def conditions():
 bp1=int(input("Systolic :- "))
 bp2=int(input("Diastolic :- "))
 if(bp1==120 and bp2==80): 
    speek("your blood pressure is normal")
 elif(bp1>120 and bp1<140 and bp2<=80 and bp2<90): 
    speek("your blood pressure is Elevated")
    speek("you should Adopt a Heart-Healthy Diet")
 elif(bp1>140 and bp2>90): 
    speek("your blood pressure is high")
    speek("See a Doctor")
 elif(bp1<90 and bp2>55): 
    speek("your blood pressure is low")
    speek("See a Doctor")
 elif(bp1>90 and bp1<120 and bp2>55 ): 
    speek("your blood pressure is slightly low")
    speek("you should Stay Hydrated,drink water")
 else:
    speek("you enter something wrong ")
    print("retry \n")
    conditions()
conditions()


