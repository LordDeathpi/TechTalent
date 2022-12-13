import time
def jokesfun():
    jokeval = int(input("Enter a number for a joke between 0 and 100: "))

    if (jokeval >-1 and jokeval < 11):
        print("Knock knock")
        time.sleep(1)
        print("Who's there?")
        time.sleep(1)
        print("Doctor")
        time.sleep(1)
        print("Doctor Who?")
        time.sleep(1)
        print("Yeah, how'd you guess?")
    
    elif (jokeval > 10 and jokeval < 31):
        print("What do you call a fish without eyes?")
        time.sleep(1)
        print("FSH!")
    
    elif (jokeval > 30 and jokeval < 76):
        print("What do you call a pig that does karate?")
        time.sleep(1)
        print("A pork chop!")
    
    elif (jokeval > 75 and jokeval < 101):
        print("Why don't scientists trust atoms?")
        time.sleep(1)
        print("Because they make up everything!")
    
    else:
        print("No joke here, number given is not between 0 and 100.")
        
jokesfun()