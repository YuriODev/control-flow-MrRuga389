sayhi = "Say hi."
dsayhi = "Don't say hi."
kwalk ="Run for it."
name = input("Do you know their name? yes/no").lower()
if name == "yes":
    ex = input("is it an ex?").lower()
    if ex == "yes":
        drunk = input("are you drunk?").lower()
        if drunk == "yes":
            rekindle = input("rekindle?").lower()
            if rekindle == "yes":
                print(sayhi)
            else:
                print(dsayhi)
        else:
            enem = input("enemy?").lower()
            if enem == "yes":
                convert = input("u in a convertible?").lower()
                if convert == "yes":
                    print(sayhi)
                else:
                    print(dsayhi)
       
    else:
        fex = input("is it a friends ex?").lower()
        if fex == "no":
            enem = input("enemy?").lower()
            if enem == "yes":
                convert = input("u in a convertible?").lower()
                if convert == "yes":
                    print(sayhi)
                else:
                    print(dsayhi)
            else:
                rob = input("u gonna rob a place?").lower()
                if rob == "yes":
                    print(dsayhi)
                else:
                    bath = input(" are you in a bathrobe?").lower()
                    if bath == "yes":
                        print(dsayhi)
                    else:
                        print(sayhi)
        else:
            print(dsayhi)
else:
    time = input("is there time to flee?").lower()
    if time == "yes":
        print(kwalk)
    else:
        pcall = input("can you pretend call?").lower()
        if pcall == "yes":
            print("Hello, doctor. What are my test results?")
        else:
            sung = input("are you wearing the glasses of sun?").lower()
            if sung == "yes":
                print("Keep walking.")
            else:
                print("Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster.'")