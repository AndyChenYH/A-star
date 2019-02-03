from matrix import Matrix
import utils
from settings import Settings
from node import Node
import time
import pygame
import sys
from random import randint as rd

def aStar():

	start = Node(Settings.startX, Settings.startY, explored=1)
	finish = Node(Settings.finishX, Settings.finishY, explored=Settings.finishExplored)

	Matrix.matrix[start.y][start.x].explored = start.explored
	Matrix.matrix[finish.y][finish.x].explored = finish.explored

	Matrix.matrix[start.y][start.x].blocksTravelled = 0

	gridSize = 30
	pygame.init()
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', round(gridSize/2))
	screen = pygame.display.set_mode([Settings.screenWidth, Settings.screenHeight])
	pygame.display.set_caption('A*')


	def drawRects():
		color = None
		for row in Matrix.matrix:
			for node in row:
				
				if node.explored == 1:
					color = (200, 100, 0)
				elif node.explored == 0:
					color = (255, 255, 255)
				elif node.explored == Settings.finishExplored:
					color = (100, 0, 0)
				elif node.explored == 10:
					color = (0, 255, 0)
				elif node.explored == 50:
					color = (130, 200, 20)
				elif node.explored == 69:
					color = (100, 100, 100)

				pygame.draw.rect(screen, color, [node.x*gridSize, node.y*gridSize, gridSize, gridSize], 0)

	def randFill():
		for row in Matrix.matrix:
			for node in row:
				if rd(0, 2) == 0:
					Matrix.matrix[node.y][node.x].explored = Settings.obstacleExplored

	

	#starting sequence
	done = False
	while not done:
		if pygame.mouse.get_pressed()[0]:
			try:
				mouseX, mouseY = pygame.mouse.get_pos()
				Matrix.matrix[round(mouseY/gridSize)][round(mouseX/gridSize)].explored = 69
			except:
				pass

		drawRects()
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					done = True
			if event.type == pygame.QUIT:
				sys.exit()

	Matrix.matrix[start.y][start.x].explored = start.explored
	Matrix.matrix[finish.y][finish.x].explored = finish.explored

	iterations = 0
	while Matrix.matrix[finish.y][finish.x].explored != 1:

		edgeNodes = utils.findEdgeNodes(Matrix.matrix)
		if edgeNodes:
			costs = []
			for node in edgeNodes:
				costs.append(node.totalCost)
			minIndex = costs.index(min(costs))
			minNode = edgeNodes[minIndex]
			Matrix.matrix[minNode.y][minNode.x].explored = 1
			Matrix.matrix[minNode.y][minNode.x].blocksTravelled = minNode.blocksTravelled + 1




		drawRects()

		iterations += 1

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()





	positionX = Settings.startX
	positionY = Settings.startY
	
	for lala in range(30):#while Matrix.matrix[finish.y][finish.x].explored != 50:
		costs = []
		pathNodes = []
		try:
			if positionX > 0:
				left = Matrix.matrix[positionY][positionX-1]
				if left.explored == 1 and left.explored != Settings.obstacleExplored:
					costs.append(left.blocksTravelled)
					pathNodes.append(left)
		except:
			pass

		try:
			right = Matrix.matrix[positionY][positionX+1]
			if right.explored == 1 and right.explored != Settings.obstacleExplored:
				costs.append(right.blocksTravelled)
				pathNodes.append(right)
		except:
			pass

		try:
			if positionY > 0:
				up = Matrix.matrix[positionY-1][positionX]
				if up.explored == 1 and right.explored != Settings.obstacleExplored:
					costs.append(up.blocksTravelled)
					pathNodes.append(up)
		except:
			pass

		try:
			down = Matrix.matrix[positionY+1][positionX]
			if down.explored == 1 and down.explored != Settings.obstacleExplored:
				costs.append(down.blocksTravelled)
				pathNodes.append(down)
		except:
			pass

		if costs:
			minIndex = costs.index(min(costs))
			nextNode = pathNodes[minIndex]

			positionX, positionY = [nextNode.y, nextNode.x]

			Matrix.matrix[positionY][positionX].explored = 50

		drawRects()
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	


aStar()



Matrix.draw()




while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
