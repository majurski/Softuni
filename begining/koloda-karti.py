from itertools import chain

#broi = int(input())
#indexes = input().split()

broi = 5
indexes = [3,3,2]
koloda = [i for i in range(1, broi+1)]

class Shuffle:
	"""docstring for rotate"""
	def __init__(self, koloda, broi):
		self.broi = broi
		self.koloda = koloda
		
	def razpred(index):
		for i in index:
			kupchina1 = koloda[:i]
			kupchina2 = koloda[i:]
			return kupchina1, kupchina2

	def chainer(kupchina1, kupchina2):
		list(chain(*zip(kupchina1,kupchina2)))












