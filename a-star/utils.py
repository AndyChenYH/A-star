import math
from settings import Settings
import math
#testy

finishExplored = Settings.finishExplored
obstacleExplored = Settings.obstacleExplored

def distanceOf(point1, point2):
	dx = abs(point1[0] - point2[0])
	dy = abs(point1[1] - point2[1])
	return math.sqrt(dx ** 2 + dy ** 2)

def findEdgeNodes(matrix):
	edgeNodes = []
	for row in matrix:
		for node in row:
			if node.explored == 1:
				try:
					if node.x > 0:
						left = matrix[node.y][node.x-1]
						if (left.explored != 1) and left.explored != obstacleExplored:
							if left.blocksTravelled == math.inf:
								left.blocksTravelled = node.blocksTravelled + 1
							edgeNodes.append(left)
				except:
					pass

				try:
					right = matrix[node.y][node.x+1]
					if (right.explored != 1) and right.explored != obstacleExplored:	
						if right.blocksTravelled == math.inf:
								right.blocksTravelled = node.blocksTravelled + 1
						edgeNodes.append(right)
				except:
					pass

				try:
					if node.y != 0:
						up = matrix[node.y-1][node.x]
						if (up.explored != 1) and up.explored != obstacleExplored:
							if up.blocksTravelled == math.inf:
								up.blocksTravelled = node.blocksTravelled + 1
							edgeNodes.append(up)
				except:
					pass

				try:
					down = matrix[node.y+1][node.x]
					if (down.explored != 1) and down.explored != obstacleExplored:
						if down.blocksTravelled == math.inf:
								down.blocksTravelled = node.blocksTravelled + 1	
						edgeNodes.append(down)
				except:
					pass

				

			
				
	return edgeNodes









































































































'''
				try:
					if node.x > 0 and node.y > 0:
						leftUp = matrix[node.y-1][node.x-1]
						if leftUp.explored != 1 and leftUp.explored != obstacleExplored:
							edgeNodes.append(leftUp)
				except:
					pass
				
				try:
					if node.y > 0:
						rightUp = matrix[node.y-1][node.x+1]
						if rightUp.explored != 1 and rightUp.explored != obstacleExplored:
							edgeNodes.append(rightUp)
				except:
					pass

				try:
					if node.x > 0:
						leftDown = matrix[node.y+1][node.x-1]
						if leftDown.explored != 1 and leftDown.explored != obstacleExplored:
							edgeNodes.append(leftDown)
				except:
					pass

				try:
					rightDown = matrix[node.y+1][node.x+1]
					if rightDown.explored != 1 and rightDown.explored != obstacleExplored:
						edgeNodes.append(rightDown)
				except:
					pass
'''




