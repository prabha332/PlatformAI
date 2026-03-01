# Main AI Orchestrator
from collectors.kube_collector import get_failed_pods
from ai_engine.fix_suggester import suggest_fix

pods = get_failed_pods()

for pod in pods:
    print("Pod:", pod["name"])
    print("Fix:", suggest_fix(pod["status"]))
