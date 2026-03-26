from flask import Flask, render_template_string
from platformctl.services.deployment_service import list_deployments
from platformctl.monitoring.health import check_cluster_health

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PlatformCTL Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial; background: #0f172a; color: white; text-align: center; }
        .card { background: #1e293b; padding: 20px; margin: 20px; border-radius: 10px; }
        h1 { color: #38bdf8; }
        .green { color: #22c55e; }
        .red { color: #ef4444; }
    </style>
</head>
<body>

<h1>🚀 PlatformCTL Dashboard</h1>

<div class="card">
    <h2>Deployments</h2>
    <p>Total: {{ total }}</p>
    <p class="green">Successful: {{ success }}</p>
    <p class="red">Failed: {{ failed }}</p>
    <p>Namespaces: {{ namespaces }}</p>
</div>

<div class="card">
    <h2>Cluster Health</h2>
    <p>Status: <span class="green">{{ health.status }}</span></p>
    <p>Score: {{ health.health_score }}%</p>
</div>

</body>
</html>
"""

@app.route("/")
def dashboard():
    deployments = list_deployments()

    total = len(deployments)
    success = len([d for d in deployments if d.status == "SUCCESS"])
    failed = len([d for d in deployments if d.status == "FAILED"])
    namespaces = len(set([d.namespace for d in deployments]))

    health = check_cluster_health()

    return render_template_string(
        TEMPLATE,
        total=total,
        success=success,
        failed=failed,
        namespaces=namespaces,
        health=health
    )

def run_web():
    app.run(host="0.0.0.0", port=5000)
