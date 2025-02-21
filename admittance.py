# Marvish Chandra

def calculateGPA():
    hGPA = 0
    eGPA = 0 # increment from here and add it to other if branches
    mGPA = 0
    sGPA = 0
    oGPA = 0
    vGPA = 0
    eGPA = 0

    history1 = input("What grade did you receive in the class?")
    if history1 == "C-":
        hGPA += 2
        history1Honors = input("Was this an honors class?")
        if history1Honors == "yes":
            hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "D":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "D-":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    history2 = input("What grade did you receive in the class?")
    if history2 == "C-":
        hGPA += 2
        history2Honors = input("Was this an honors class?")
        if history2Honors == "yes":
            hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "D":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "D-":
        hGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif history2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    english1 = input("What grade did you receive in the class?")
    if english1 == "C-":
        eGPA += 2
        english1Honors = input("Was this an honors class?")
        if english1Honors == "yes":
            eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english1 == "D":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english1 == "D-":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    english2 = input("What grade did you receive in the class?")
    if english2 == "C-":
        eGPA += 2
        english2Honors = input("Was this an honors class?")
        if english2Honors == "yes":
            eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english2 == "D":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english2 == "D-":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    english3 = input("What grade did you receive in the class?")
    if english3 == "C-":
        eGPA += 2
        english3Honors = input("Was this an honors class?")
        if english3Honors == "yes":
            eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english3 == "D":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english3 == "D-":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english3 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    english4 = input("What grade did you receive in the class?")
    if english4 == "C-":
        eGPA += 2
        english4Honors = input("Was this an honors class?")
        if english4Honors == "yes":
            eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english4 == "D":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english4 == "D-":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif english4 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    math1 = input("What grade did you receive in the class?")
    if math1 == "C-":
        mGPA += 2
        math1Honors = input("Was this an honors class?")
        if math1Honors == "yes":
            mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math1 == "D":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math1 == "D-":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    math2 = input("What grade did you receive in the class?")
    if math2 == "C-":
        mGPA += 2
        math2 = input("Was this an honors class?")
        if math2 == "yes":
            mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math2 == "D":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math2 == "D-":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    math3 = input("What grade did you receive in the class?")
    if math3 == "C-":
        mGPA += 2
        math3Honors = input("Was this an honors class?")
        if math3Honors == "yes":
            mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math3 == "D":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math3 == "D-":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math3 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    math4 = input("What grade did you receive in the class?")
    if math4 == "C-":
        mGPA += 2
        math4Honors = input("Was this an honors class?")
        if math4Honors == "yes":
            mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math4 == "D":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math4 == "D-":
        mGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif math4 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    science1 = input("What grade did you receive in the class?")
    if science1 == "C-":
        sGPA += 2
        science1Honors = input("Was this an honors class?")
        if science1Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    science2 = input("What grade did you receive in the class?")
    if science2 == "C-":
        sGPA += 2
        science2Honors = input("Was this an honors class?")
        if science2Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    science3 = input("What grade did you receive in the class?")
    if science3 == "C-":
        sGPA += 2
        science3Honors = input("Was this an honors class?")
        if science3Honors == "yes":
            sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "D":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "D-":
        sGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif science3 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    otherLang1 = input("What grade did you receive in the class?")
    if otherLang1 == "C-":
        oGPA += 2
        otherLang1 = input("Was this an honors class?")
        if otherLang1 == "yes":
            oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang1 == "D":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang1 == "D-":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    otherLang2 = input("What grade did you receive in the class?")
    if otherLang2 == "C-":
        oGPA += 2
        otherLang2Honors = input("Was this an honors class?")
        if otherLang2Honors == "yes":
            oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang2 == "D":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang2 == "D-":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang2 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    otherLang3 = input("What grade did you receive in the class?")
    if otherLang3 == "C-":
        oGPA += 2
        otherLang3Honors = input("Was this an honors class?")
        if otherLang3Honors == "yes":
            oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang3 == "D":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang3 == "D-":
        oGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif otherLang3 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    visualArt1 = input("What grade did you receive in the class?")
    if visualArt1 == "C-":
        vGPA += 2
        visualArt1Honors = input("Was this an honors class?")
        if visualArt1Honors == "yes":
            vGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif visualArt1 == "D":
        vGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif visualArt1 == "D-":
        vGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif visualArt1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elective1 = input("What grade did you receive in the class?")
    if elective1 == "C-":
        eGPA += 2
        elective1Honors = input("Was this an honors class?")
        if elective1Honors == "yes":
            eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "D":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "D-":
        eGPA += 1
        print("You cannot be admitted because your grade is lower than a C in the class.")
    elif elective1 == "F":
        print("You cannot be admitted because your grade is lower than a C in the class.")
    calculatedGPA = 15 / (hGPA + eGPA + mGPA + sGPA + oGPA + vGPA + eGPA)
    print("Your calculated UC GPA is: ",calculatedGPA)