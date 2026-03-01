#  Self-Healing Automation
import subprocess

def restart_deployment(name, namespace):

    cmd = [
        "kubectl",
        "rollout",
        "restart",
        f"deployment/{name}",
        "-n",
        namespace
    ]

    subprocess.run(cmd)
