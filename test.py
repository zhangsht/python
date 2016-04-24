def yh():
	N = [1]
	x = 9
	while x > 0:
		yield N
		N.append(0)
		N = [N[i - 1] + N[i] for i in range(len(N))]
		x = x - 1

def add(x, y, func):
	return func(x) + func(y)

print("{}{}" .format("hello", "world"))
print("{0}{1}" .format("hello", "world"))
print("{0}{1}{0}" .format("hello", "world"))

data = {'name':'python', 'score':100}
print("Name: {0[name]}, Socre:{0[score]}" .format(data))

print("{0:,}" .format(1.25e6))

def normalize(s):
	return s[0].upper()+s[1:].lower()

def normalize(s):
	return s.capitalize()

def prod(L):
	def fn(x, y):
		return x * y
	return reduce(fn, L)

def str2float(s):
	ss = s.replace('.', '')
	def fn(x, y):
		return 10 * x + y
	def char2num(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	return reduce(fn, map(char2num, ss)) / (10 ** (len(s) - s.index('.') - 1))

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

def is_palidrome(n):
	oldStr = str(n)
	newStr = ''
	for c in oldStr:
		newStr = c + newStr
	return newStr == oldStr
filter(is_palidrome, range(1,100))