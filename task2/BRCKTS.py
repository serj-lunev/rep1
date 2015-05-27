import sys
f = open(sys.argv[1])
class bracket:
	def __init__(self, ex):
		self.exp = ex
	def change(self, i):
		if self.exp[i - 1] == ')':
			self.exp = self.exp[:i - 1] + '(' + self.exp[i-1:]
		else : 
			self.exp = self.exp[:i - 1] + ')' + self.exp[i-1:]
	def check(self):
		i = 0
		p = 0
		while i < len(self.exp) and p >= 0:
			if self.exp[i] == '(':
				p += 1
			else :
				p -= 1
			i += 1
		if p == 0:
			print("YES")
		else :
			print("NO")
i = 1
while i <= 10:
	f.readline()
	br = bracket(f.readline())
	M = int(f.readline())
	print("Test %d:" % i)
	j = 0
	while j < M:
		k = int(f.readline())
		if k == 0:
			br.check()
		else :
			br.change(k)
		j += 1	
	i += 1
