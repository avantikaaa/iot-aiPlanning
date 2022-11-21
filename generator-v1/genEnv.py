towers = 2
floors = 2
rooms = 2

f = open("env_file", "w")

for t in range(towers):
	t_name = "t" + str(t+1)
	for fl in range(floors):
		f_name = t_name + "f" + str(fl+1)
		f.write("in " + t_name + " " + f_name + "\n")
		for r in range(rooms):
			r_name = f_name + "r" + str(r+1)
			f.write("in " + f_name + " " + r_name + "\n")

f.close()