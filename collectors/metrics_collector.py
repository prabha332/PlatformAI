# Simulated Prometheus-style metrics collector

import random
from utils.logger import logger


def get_pod_metrics(pod, namespace):

    try:
        metrics = {
            "cpu": random.randint(10, 95),
            "memory": random.randint(100, 900),
            "restarts": random.randint(0, 10)
        }

        logger.info(
            f"Metrics collected for {pod}"
        )

        return metrics

    except Exception as e:
        logger.error(e)

        return {
            "cpu": 0,
            "memory": 0,
            "restarts": 0
        }
