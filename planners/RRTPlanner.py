import sys
import time
from typing import Any

import numpy as np

from environments.EnvironmentBase import EnvironmentBase
from planners.RRTPlannerBase import RRTPlannerBase
from planners.PlanResult import PlanResult


class RRTPlanner(RRTPlannerBase):
    def __init__(
            self,
            planning_env: EnvironmentBase,
            seed: int,
            bias: float = 0.05,
            eta: float = 1.0,
            max_iter: int = 10000):
        RRTPlannerBase.__init__(
            self,
            planning_env=planning_env,
            bias=bias,
            max_iter=max_iter,
            seed=seed)
        self.eta = eta  # Distance to extend

    def plan(
            self,
            start_config: np.ndarray,
            goal_config: np.ndarray) -> PlanResult:
        # TODO: YOUR IMPLEMENTATION HERE

        plan_time = time.time()

        # Start with adding the start configuration to the tree.
        self.tree.AddVertex(start_config)

        plan = []
        plan.append(start_config)
        plan.append(goal_config)

        cost = 0
        plan_time = time.time() - plan_time

        print("Cost: %f" % cost)
        print("Planning Time: %ds" % plan_time)

        return PlanResult(
            plan=np.concatenate(plan, axis=1),
            cost=cost,
            time=plan_time)

    def extend(
            self,
            x_near: np.ndarray,
            x_rand: np.ndarray) -> Any:
        # TODO: YOUR IMPLEMENTATION HERE
        return x_near
