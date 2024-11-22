from flask import Flask
import random
import json

app = Flask(__name__)



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


@app.route("/")
def generate_data():
    
    res = {}
    for i in range(len(matieres)):
        res[i]["ObjectId"] = i + 1
        res[i]["nameUe"] = list(matieres.keys())[i]
        res[i]["ects"] = matieres[list(matieres.keys())[i]]["ects"]
        res[i]["list"] = {"name" : j, "grade":random.randint(0, 20) for j in matieres["list"][i]}
        
    file = json.dumps(res)
    print(file)
    return file
