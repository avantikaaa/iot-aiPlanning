import json
from data_utils import getPredicates, getActions, constructInit

with open('./env_v1.json') as f:
   data = json.load(f)

f = open("./generated_domain.pddl", "w")

f.write(f'(define (domain {data["domain_name"]}) \n')

domain_predicates = getPredicates(data)

f.write(f'(:predicates ')
for obj in domain_predicates:
    f.write(f'\t{obj}\n')
f.write(')\n')

target_actions, implementation = getActions('action_impl.json')

for obj in target_actions:
    f.write(f'\t(:action {obj}\n')
    for i in implementation[obj]:
        f.write(f'\t{i}\n')
    f.write('\t)\n\n')


f.write(')')
f.close()