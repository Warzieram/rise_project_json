import random
import json




matieres = {
    "Langues": {
        "list":[
            "Langues"
        ], 
        "ects":3},
    "GPU computing":{
        "list":[
            "Programmation parrallèle, OpenGL",
            "Algorithms",
            "Image Processing Lab"
        ],
        "ects":6
    },
    "Architecture and software quality":{
        "list":[
            "Software Architecture",
            "Software Architecture and Quality Lab"
        ],
        "ects":4
    },
    "Database management system":{
        "list":[
            "Relationnal Database",
            "Realtime DB, NoSQL, XML"
        ],
        "ects":4
    },
    "Computer Network":{
        "list":[
            "Fieldbuses and industrial Ethernet",
            "Network concepts",
            "Computer Network Lab"
        ],
        "ects":5
    },
    "IOT and data acquisition":{
        "list":[
            "IoT Lab",
            "Instrumentation Lab",
            "Instrumentation"
        ],
        "ects":4
    },
    "Gestion 1":{
        "list":[
            "Projet - qualité",
            "Science humaines",
            "Ethics Lab"
        ],
        "ects":6
    },
}


def generate_data():
    
    l = []
    for i in range(len(matieres)):
        res = {}
        current_key = list(matieres.keys())[i]
        ects = matieres[current_key]["ects"]
        res["ObjectId"] = i + 1
        res["nameUe"] = current_key
        res["ects"] = ects
        res["list"] = [{"name" : j, "grade": random.randint(0, 20)} for j in matieres[current_key]["list"]]
        n = len(res["list"])
        k = 0
        addin = ects // n if ects % 2 == 0 or n == 1 else ects // (n-1)
        print(ects, n, addin)
        for j in res["list"]:
            k += 1
            if (k == n) and (ects % 2 != 0):
                j["ectsNumber"] = 1
            else:
                j["ectsNumber"] = addin
            

        l.append(res)
    file = json.dumps(l)
    print(file)
    return file



j = generate_data()

with open("test.json", "w") as outfile:
    outfile.write(j)
