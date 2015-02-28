import random
import string

def gen_token():
	N = 6
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))


if __name__ == "__main__":
	print gen_token()