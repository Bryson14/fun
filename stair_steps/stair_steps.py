import sys


def validate_perm(a, N):
	if sum(a) == N:
		print(a)


def perm(a, length, n, N):
	if length == 1:
		validate_perm(a, N)

	for i in range(length):
		perm(a, length - 1, n, N)

		if length & 1:
			a[0], a[length - 1] = a[length - 1], a[0]
		else:
			a[i], a[length - 1] = a[length - 1], a[i]


def main(N, steps_at_a_time=[1,2]):
	if min(steps_at_a_time) > N:
		print(f'No possible combination to climb {N} stairs in {min(steps_at_a_time)} step leaps')
	#  do a recursive call and pick on number from the set at a time. Exhaust all posiblities one step at a time. If already tried, add to a set and keep moving on
	else:
		size = len(steps_at_a_time)
		perm(steps_at_a_time, size, size, N)




if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(int(sys.argv[1]))
	elif len(sys.argv) == 3:
		main(int(sys.argv[1]), [int(i) for i in str(sys.argv[2]).split(',')])
	else:
		print("USAGE: stair_step.py NSTEPS [AVAILABLE NUMBER OF STEPS TO WALK]")
		print("i.e. if you want the person to only be able to walk 1, 3, or 4 stair at a time use...")
		print('stair_step.py 15 1,3,4')
