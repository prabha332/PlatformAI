# Kubernetes Failure Collector
from kubernetes import client, config

def get_failed_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    failed = []

    pods = v1.list_pod_for_all_namespaces()

    for pod in pods.items:
        phase = pod.status.phase

        if phase != "Running":
            failed.append({
                "name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "status": phase
            })

    return failed
