import logging

import numpy as np

from typing import Type

from core.max_flow import MaxFlow, FordFulkerson, EdmondsKarp
from core.network import generate_random_rnetwork_bernoulli
from core.utils import timeit


logger = logging.getLogger(__name__)


def random_run(
        algorithm: Type[MaxFlow],
        max_iter: int,
        node_n: int,
        threshold: int,
        min_cap: int,
        max_cap: int,
) -> None:
    mf = algorithm()
    rn = generate_random_rnetwork_bernoulli(node_n=node_n, threshold=threshold, min_cap=min_cap, max_cap=max_cap)
    mf.process_network(rn, max_iter=max_iter)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    tests_num = 100
    params = dict(max_iter=1_000, node_n=100, threshold=0.03, min_cap=1, max_cap=250)

    ff_mean = np.mean([timeit(random_run)(FordFulkerson, **params)[0] for _ in range(tests_num)])
    ek_mean = np.mean([timeit(random_run)(EdmondsKarp, **params)[0] for _ in range(tests_num)])
    logger.info(f"Ford-Fulkerson mean time on random instances: {ff_mean:.3f}")
    logger.info(f"Edmonds-Karp mean time on random instances: {ek_mean:.3f}")
