def parseEnv(env_file):
	f = open(env_file, 'r')
	predicates = set()
	init = []
	objects = set()
	for line in f.readlines():
		line = line.strip("\n")
		init.append("(" + line + ")")
		line = line.split()
		for obj in line[1:]:
			objects.add(obj)
		pred = "(" + line[0]
		# print(line)
		for var in range(len(pred)-1):
			pred += " ?var" + str(var)
		predicates.add(pred + ")")
		# break
	actions = getActions(list(objects))
	predicates = "\n".join(list(predicates))
	objects = " ".join(list(objects))
	return predicates, objects, "\n".join(init), actions

def getActions(objects):
	actions = []
	return actions
	for obj in objects:
		js = obj.actions()
		# parse json: {name: action_name, parameters: "(...)", precondition: "(...)", effect: "(...)"}



p, o, i, a = parseEnv("env_file")
print(p)
print(o)
print(i)