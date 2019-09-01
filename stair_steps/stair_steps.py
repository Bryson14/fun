import sys


def verify_str_step(steps):
	s = 0
	for char in steps:
		s += int(char)
	return s


def main(n, x):
	og = []
	cache = []
	solved = False
	for step in x:
		og.append(str(step))

	while not solved:

		for i in range(len(og)):
			base = og[i]
			new_steps = stepper(n, x, base)
			if new_steps:
				for new in new_steps:
					cache.append(new)
			else:
				cache.append(base)

		og = cache[:]  #passed by value
		cache = []

		solved = True
		for pos in og:
			if verify_str_step(pos) >= n:
				pass
			else:
				solved = False
	print(og)


def stepper(n, x, base):
	modified = []
	for i in range(len(x)):
		if verify_str_step(base + str(x[i])) <= n:
			modified.append(base + str(x[i]))
		else:
			#  new addition would make it too big
			pass
	return modified


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(int(sys.argv[1]), [1, 2])
	elif len(sys.argv) > 2:
		main(int(sys.argv[1]), [int(i) for i in sys.argv[2:]])
	else:
		print("USAGE: stair_step.py NSTEPS [AVAILABLE NUMBER OF STEPS TO WALK]")
		print("i.e. if you want the person to only be able to walk 1, 3, or 4 stair at a time use...")
		print('stair_step.py 15 1 3 4')
