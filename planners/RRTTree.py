from typing import List, Dict, Tuple

import numpy as np


class RRTTree:
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.vertices: List[np.ndarray] = []
        self.costs: List[float] = []
        self.edges: Dict[int, int] = dict()

    def GetRootID(self) -> int:
        """ Return the ID of the root in the tree.
        """
        return 0

    def GetNearestVertex(
            self,
            config: np.ndarray) -> Tuple[int, np.ndarray]:
        """ Return the nearest state ID in the tree.

            @param config: Sampled configuration.
        """
        ver = np.concatenate(self.vertices, axis=1)  # dim_vertex, num_vertices
        idx = (np.linalg.norm(ver - config, axis=0)).argmin()
        return idx, ver[:, idx].reshape(ver.shape[0], 1)

    def GetNNInRad(
            self,
            config: np.ndarray,
            rad: float) -> Tuple[List[int], List[np.ndarray]]:
        """ Return neighbors within ball of radius. Useful for RRT*

            @param config: Sampled configuration.
            @param rad ball radius
        """
        ver = np.concatenate(self.vertices, axis=1)
        indexes = np.linalg.norm(ver - config, axis=0) < rad
        vids = np.nonzero(indexes)[0].tolist()
        vertices = np.transpose(ver[:, indexes], (1, 0))  # num_vertices, dim_vertex
        vertices = vertices.reshape(vertices.shape[0], vertices.shape[1], 1)  # num_vertices, dim_vertex, 1
        return vids, vertices

    def AddVertex(
            self,
            config: np.ndarray,
            cost: float = 0.) -> int:
        """ Add a state to the tree.

            @param config Configuration to add to the tree.
        """
        vid = len(self.vertices)
        self.vertices.append(config)
        self.costs.append(cost)
        return vid

    def AddEdge(self, sid, eid):
        """ Adds an edge in the tree.

            @param sid start state ID.
            @param eid end state ID.
        """
        self.edges[eid] = sid
