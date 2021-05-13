import numpy as np

from environments.EnvironmentBase import EnvironmentBase
from planners.PlannerBase import PlannerBase
from planners.PlanResult import PlanResult


class AStarPlanner(PlannerBase):
    def __init__(
            self,
            planning_env: EnvironmentBase,
            epsilon: float):
        PlannerBase.__init__(
            self,
            planning_env=planning_env)
        self.nodes = {}
        self.epsilon = epsilon
        self.visited = np.zeros(self.env.map.shape)

    def plan(
            self,
            start_config: np.ndarray,
            goal_config: np.ndarray) -> PlanResult:
        # TODO: YOUR IMPLEMENTATION HERE

        plan = []
        plan.append(start_config)
        plan.append(goal_config)

        state_count = 0
        cost = 0

        print("States Expanded: %d" % state_count)
        print("Cost: %f" % cost)

        return PlanResult(
            plan=np.concatenate(plan, axis=1),
            cost=cost,
            num_states=state_count)
