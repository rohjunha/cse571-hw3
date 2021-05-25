import time
from pathlib import Path

import numpy as np
import pytest
from environments.MapEnvironment import MapEnvironment


@pytest.fixture
def MAP_FILE():
    return Path(Path(__file__).parent, '../maps/map2.txt')

@pytest.fixture
def START():
    return np.array([321, 148]).reshape(2, 1)

@pytest.fixture
def GOAL():
    return np.array([106, 202]).reshape(2, 1)


def test_sample(MAP_FILE, START, GOAL):
    map_env = MapEnvironment(map_file=MAP_FILE,
                             start=START,
                             goal=GOAL,
                             seed=2021)
    start = time.time()
    n_samples = 10000
    for _ in range(n_samples):
        map_env.sample()
    end = time.time()
    print(f"elapsed time: {end - start} for {n_samples} samples")

