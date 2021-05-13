import numpy as np

from environments.EnvironmentBase import EnvironmentBase
from planners.PlanResult import PlanResult


class PlannerBase:
    def __init__(self, planning_env: EnvironmentBase):
        self.env = planning_env

    def plan(
            self,
            start_config: np.ndarray,
            goal_config: np.ndarray) -> PlanResult:
        raise NotImplementedError
