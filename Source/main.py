from SearchAlgorithms import *
import argparse
import pygame
import time

def main(algo:str, start_pos:int, goal_pos:int):
    pygame.init()
    pygame.display.set_caption(f'<Huỳnh Lưu Vĩnh Phong (21280103) - Trần Thị Uyên Nhi (21280125)> - {algo}')
    sc = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color('black'))

    g = Graph(start_pos, goal_pos)
    g.draw(sc)
    clock.tick(200)
    

    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    elif algo == 'UCS':
        UCS(g, sc)
    elif algo == "DIJ":
        Dijkstra(g, sc)
    elif algo == "AStar":
        AStar(g, sc)
    else:
        raise NotImplementedError('Not implemented')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Search algorithms')
    parser.add_argument('--algo', type=str, help='Enter search algorithm', default='DFS')
    parser.add_argument('--start', type=int, help='Enter start position', default=71) #71
    parser.add_argument('--goal', type=int, help='Enter goal position', default=318) #318

    args = parser.parse_args()
    main(args.algo, args.start, args.goal)
