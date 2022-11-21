import json
from data_utils import getPredicates, getActions, constructInit

with open('./env_v2.json') as f:
   data = json.load(f)

f = open("./generated_domain.pddl", "w")

f.write(f'(define (domain {data["domain_name"]}) \n')

# print(getPredicates(data))

domain_predicates = getPredicates(data)

f.write(f'(:predicates ')
for obj in domain_predicates:
    f.write(f'{obj}')
f.write(')\n')

domain_actions = getActions(data)



# f.write(f'(:action ')
for obj in domain_actions:
    f.write(f'{obj}')
# f.write(')\n')

# f.write('(:init ')
# init_state = constructInit(data)
# f.write(f'{init_state})\n')

# f.write('(:goal ')
# goal = getProblemGoal(data)
# f.write(f'{goal})\n')
f.write(')')
f.close()