# Collect logs directly from Kubernetes

from kubernetes import client, config
from utils.logger import logger


config.load_kube_config()
v1 = client.CoreV1Api()


def get_pod_logs(pod, namespace):

    try:
        logs = v1.read_namespaced_pod_log(
            name=pod,
            namespace=namespace,
            tail_lines=100
        )

        return logs

    except Exception as e:
        logger.error(f"Log collection failed: {e}")
        return "No logs available"
