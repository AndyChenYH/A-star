import utils
from settings import Settings
import math
class Node():
	def __init__(self, x, y, explored=0):
		self.x = x
		self.y = y
		self.blocksTravelled = math.inf #by default
		
		bfs = utils.distanceOf([self.x, self.y], [Settings.startX, Settings.startY])
		self.blocksFromStart = bfs
		btf = utils.distanceOf([self.x, self.y], [Settings.finishX, Settings.finishY])
		self.blockToFinish = btf
		
		self.totalCost = btf

		self.explored = explored
