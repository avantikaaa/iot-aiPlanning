import json
def parseProblemObjects(data) -> list:
    objects = [i['name'] for i in data['problem_objects']]
    return objects

def constructInit(data) -> str:
    res = ''
    for i in data['init']:
        res+=(f'\t{i}\n')
    return res

def getProblemGoal(data) -> str:
    res = ''
    for i in data['goal']:
        res+=(f'\t{i}\n')
    return res

def getPredicates(data) -> str:
    res = []
    for obj in data['predicates']:
        if obj['extensible']:
            f = open(obj["type"] + ".device.json", "r")
            d = json.load(f)
            # print(d)
            for i in d["predicates"]:
                # print(i)
                res.append(i)
    return res

def getActions(data) -> str:
    res = ''
    for obj in data['predicates']:
        if obj['extensible']:
            f = open(obj["type"] + ".device.json", "r")
            d = json.load(f)
            for i in d["actions"]:
                res += '''(:action %s
\t:parameters %s
\t:precondition %s
\t:effect %s''' % (i["name"], i["parameters"], i["precondition"], i["effect"]) + ")\n"
    return res