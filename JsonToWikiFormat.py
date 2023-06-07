import json

def run(jsonFile):
    def checkForSubStuff(a):
        if "(" in a:
            lst = a.split(" (")
            return "[[" + str(lst[0]) + "]] (" + lst[1]
        else:
            return "[[" + a + "]]"


    with open(jsonFile, 'r') as myfile:
        data=myfile.read()

    obj = json.loads(data)

    for i in obj:
        print("|-")
        print("| " + i)

        string = ""
        counter = 0

        for a in obj[i]:
            if counter != 0:
                a = checkForSubStuff(a)
                string += ", " + a
            else:
                a = checkForSubStuff(a)
                string += "| " + a
            counter += 1
        print(string)