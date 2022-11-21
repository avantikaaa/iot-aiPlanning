import json
from data_utils import parseProblemObjects, constructInit, getProblemGoal

with open('./env_v2.json') as f:
   data = json.load(f)

f = open("./generated_problem.pddl", "w")

f.write(f'(define (problem {data["problem_name"]}) \n')
f.write(f'(:domain {data["domain_name"]}) \n')

problem_objects = parseProblemObjects(data)

f.write(f'(:objects ')
for obj in problem_objects:
    f.write(f'{obj} ')
f.write(')\n')

f.write('(:init ')
init_state = constructInit(data)
f.write(f'{init_state})\n')

f.write('(:goal ')
goal = getProblemGoal(data)
f.write(f'{goal})\n')
f.write(')')
f.close()