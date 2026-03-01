# ai_engine/analyzer.py

from collectors.kube_collector import get_failed_pods
from collectors.logs_collector import get_pod_logs
from collectors.metrics_collector import get_pod_metrics
from ai_engine.fix_suggester import suggest_fix
from ai_engine.predictor import predict
from utils.logger import logger


def analyze_cluster():

    analysis_results = []

    failed_pods = get_failed_pods()

    logger.info(f"Detected {len(failed_pods)} unhealthy pods")

    for pod in failed_pods:

        name = pod["name"]
        namespace = pod["namespace"]
        status = pod["status"]

        logs = get_pod_logs(name, namespace)
        metrics = get_pod_metrics(name, namespace)

        incident_risk = predict(
            metrics["cpu"],
            metrics["memory"],
            metrics["restarts"]
        )

        fix = suggest_fix(status)

        result = {
            "pod": name,
            "namespace": namespace,
            "status": status,
            "incident_prediction": incident_risk,
            "suggested_fix": fix,
            "logs_summary": logs[:200]
        }

        analysis_results.append(result)

        logger.info(f"Analyzed pod {name}")

    return analysis_results
