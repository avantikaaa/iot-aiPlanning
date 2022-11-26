import json 
import os 

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
            f = open(obj['type'] + ".device.json", "r")
            device = json.load(f)
            for p in device['predicates']:
                res.append(p)
        res.append(f'({obj["type"]} ?{obj["param"]})')
    return res

def getActions(actions_file: str):
    device_files = []
    target_actions = []
    res = ''
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.split('.')[1] == 'device':
            device_files.append(f)    
    
    for file in device_files:
        f = open(file, 'r')
        device = json.load(f)
        for action in device['actions']:
            target_actions.append(action)
        f.close()
    
    f = open('./action_impl.json', 'r')
    actions = json.load(f)
    return target_actions, actions
