def getShortestPath(nodeN:int, edges:list, matrix:list):
    minDistances = ([[999999]*nodeN]*nodeN)
    for trueSource in range(nodeN):
        for pseudoSource in range(nodeN):
            for trueDestination in range(nodeN):
                pseudoDistance = minDistances[trueSource][pseudoSource] + matrix[pseudoDistance][trueDestination]
                trueDistance = matrix[trueSource][trueDestination]
                if pseudoDistance < trueDistance:
                    minDistances[trueSource][trueDestination] = pseudoDistance
    return minDistances



def getEdges(nodeN:int):
    edges = list()
    edgeN = int(input("Enter no. of edges : "))
    for edge in range(edgeN):
        sourceNode      = int(input(edge + " Source      : "))
        destinationNode = int(input(edge + " Destination : "))
        cost            = int(input(edge + " Cost        : "))
        edges.append([sourceNode, destinationNode, cost])
        print()
    return edges


def convertToMatrix(nodeN:int, edges:list):
    matrix = ([[0]*nodeN]*nodeN)
    for edge in edges:
        matrix[edge[0]][edge[1]] = cost
    return matrix


def main():
    nodeN = int(input("Enter no. of nodes : "))
    edges = getEdges(nodeN)
    matrix = convertToMatrix(nodeN, edgeN)
    minDistances = getShortestPath(nodeN, edges, matrix)


if __name__ = '__main__':
    main()