import random

# code adapted from the tutorial of the article "How to Implement the Hill Climbing Algorithm in Python"
# https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de


# comentários em português para melhor entendimento na aula


# gera uma solução aleatória para o problema, pegando os índices das cidades, os embaralhando e retornando em um array
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
        
    print('random arrangement: ', solution)
    return solution

# calcula o tamanho da rota a partir de uma solução e da matriz de distâncias
def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

# gera os vizinhos de uma solução, trocando duas cidades de posição no array de solução já existente
# ex: [0, 1, 2, 3, 4, 5] -> [0, 1, 3, 2, 4, 5]
def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

# retorna o melhor vizinho de uma lista de vizinhos
def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

# função principal do algoritmo, usa todas as funções anteriores para gerar a solução final
def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
    print('first solution: ', bestNeighbour , ', ', bestNeighbourRouteLength)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
        print('current solution: ', bestNeighbour , ', ', bestNeighbourRouteLength)


    return currentSolution, currentRouteLength



def main():
    # matriz de distâncias entre as cidades, representando o problema da figura do slide
    tsp = [
        [0, 200, 500, 650, 600, 150],
        [200, 0, 250, 700, 750, 300],
        [500, 250, 0, 150, 400, 500],
        [650, 700, 150, 0, 100, 200],
        [600, 750, 400, 100, 0, 150],
        [150, 300, 500, 200, 150, 0]
    ]

    print('-----')
    print('\n final solution', hillClimbing(tsp))

if __name__ == "__main__":
    main()
