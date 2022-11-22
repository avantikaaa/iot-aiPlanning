import json
from data_utils import getPredicates, getActions, constructInit

with open('./env_v2.json') as f:
   data = json.load(f)

f = open("./generated_domain.pddl", "w")

f.write(f'(define (domain {data["domain_name"]}) \n')

# print(getPredicates(data))

domain_predicates = getPredicates(data)
init_state = constructInit(data)
# print(init_state)
init_state = init_state.split("\n")
# print(init)
init = []
for i in init_state:
    # i.strip('\t')
    init.append(i[2:-1])
# init = [i.strip("\t(")[:-1] for i in init]
# print(init)
# exit()
init.pop()
pred = set()
for i in domain_predicates:
    pred.add(i.split()[0][1:])
# print(pred)
for i in init:
    # print(i)
    if i.split()[0].lower() not in pred:
        i = i.split()
        tmp = i[0].lower()
        # print(tmp)
        pred.add(tmp)
        for j in range(len(i)-1):
            tmp += " ?var" + str(j)
        domain_predicates.append("(" + tmp + ")")
        # print(pred)

# domain_predicates += init
f.write(f'(:predicates ')
for obj in domain_predicates:
    f.write(f'\t{obj}\n')
f.write(')\n')

domain_actions = getActions(data)



f.write(f'(:action ')
for obj in domain_actions:
    f.write(f'{obj}')
f.write(')\n')

# f.write('(:init ')
# init_state = constructInit(data)
# f.write(f'{init_state})\n')

# f.write('(:goal ')
# goal = getProblemGoal(data)
# f.write(f'{goal})\n')
f.write(')')
f.close()