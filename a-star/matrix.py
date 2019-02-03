from node import Node
from settings import Settings
import math


class Matrix():

	matrix = [[Node(x, y) for x in range(Settings.size)]
	for y in range(Settings.size)]
	def draw():

		for y in range(Settings.size):
			for x in range(Settings.size):
				if x < Settings.size:
					obj = Matrix.matrix[y][x].explored 
					if obj != math.inf:
						print('%3s' % str(round(obj)), end = ' ')
					else:
						print('%3s' % str(obj), end = ' ')

				if x == Settings.size - 1:
					print()

	def setObstable(x, y):
		Matrix.matrix[y][x].explored = Settings.obstacleExplored

