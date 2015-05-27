import sys
f = open(sys.argv[1])
f.readline()
class answer:
	def __init__(self, q):
		self.query = q
	def printing(self, x, y):
		x = x - 1
		y = y - 1
		res = int(self.query[x])
		s = 0
		while x <= y:
			s = s + int(self.query[x])
			res = max(res, s)
			s = max(s, 0)	
			x = x + 1
		print(res)
	def changing(self, x, y):
		self.query[x - 1] = y
p = answer(f.readline().split())
m = f.readline()
i = 0
while i < int(m):
	k = f.readline().split()
	if int(k[0]) == 0:
		p.changing(int(k[1]), int(k[2]))
	else :
		p.printing(int(k[1]), int(k[2]))
	i = i + 1
f.close()
