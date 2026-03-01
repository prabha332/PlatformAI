# DevOps AI API Server
from fastapi import FastAPI
from collectors.kube_collector import get_failed_pods
from ai_engine.fix_suggester import suggest_fix

app = FastAPI()

@app.get("/analyze")
def analyze():

    pods = get_failed_pods()

    results = []

    for pod in pods:
        fix = suggest_fix(pod["status"])

        results.append({
            "pod": pod["name"],
            "issue": pod["status"],
            "suggested_fix": fix
        })

    return results
