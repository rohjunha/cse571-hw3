import argparse

import matplotlib.pyplot as plt
import numpy as np

from planners.AStarPlanner import AStarPlanner
from environments.CarEnvironment import CarEnvironment
from environments.EnvironmentBase import EnvironmentBase
from environments.MapEnvironment import MapEnvironment
from planners.PlannerBase import PlannerBase
from planners.RRTPlanner import RRTPlanner
from planners.RRTPlannerNonholonomic import RRTPlannerNonholonomic
from planners.RRTStarPlanner import RRTStarPlanner


def run_planner(
        planning_env: EnvironmentBase,
        planner: PlannerBase,
        start: np.ndarray,
        goal: np.ndarray,
        argplan: str = 'astar'):
    input('Press any key to begin planning...')

    planning_env.init_visualizer()

    # Plan
    plan_result = planner.plan(start, goal)

    # Visualize the final path
    tree = None
    visited = None
    if argplan != 'astar':
        tree = planner.tree
    else:
        visited = planner.visited
    planning_env.visualize_plan(plan_result.plan, tree, visited)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='script for testing planners')

    parser.add_argument('-m', '--map', type=str, default='map1.txt',
                        help='The environment to plan on')
    parser.add_argument('-p', '--planner', type=str, default='astar',
                        help='The planner to run (astar, rrt, rrtstar, nonholrrt)')
    parser.add_argument('-s', '--start', nargs='+', type=float, required=True)
    parser.add_argument('-g', '--goal', nargs='+', type=float, required=True)
    parser.add_argument('-eps', '--epsilon', type=float, default=1.0, help='Epsilon for A*')
    parser.add_argument('-eta', '--eta', type=float, default=1.0, help='eta for RRT/RRT*')
    parser.add_argument('-b', '--bias', type=float, default=0.05, help='Goal bias for RRT/RRT*')
    parser.add_argument('--seed', type=int, default=2021, help='random seed for sampling')

    args = parser.parse_args()

    # First setup the environment and the robot.
    dim = 3 if args.planner == 'nonholrrt' else 2
    args.start = np.array(args.start).reshape(dim, 1)
    args.goal = np.array(args.goal).reshape(dim, 1)
    if args.planner == 'nonholrrt':
        planning_env = CarEnvironment(args.map, args.start, args.goal, args.seed)
    else:
        planning_env = MapEnvironment(args.map, args.start, args.goal, args.seed)

    # Next setup the planner
    if args.planner == 'astar':
        planner = AStarPlanner(planning_env, epsilon=args.epsilon)
    elif args.planner == 'rrt':
        planner = RRTPlanner(planning_env, seed=args.seed, bias=args.bias, eta=args.eta)
    elif args.planner == 'rrtstar':
        planner = RRTStarPlanner(planning_env, seed=args.seed, bias=args.bias, eta=args.eta, rad=50.)
    elif args.planner == 'nonholrrt':
        planner = RRTPlannerNonholonomic(planning_env, seed=args.seed, bias=args.bias)
    else:
        print('Unknown planner option: %s' % args.planner)
        exit(0)

    run_planner(
        planning_env=planning_env,
        planner=planner,
        start=args.start,
        goal=args.goal,
        argplan=args.planner)


if __name__ == '__main__':
    main()
