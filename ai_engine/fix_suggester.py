# AI Fix Suggestion Engine
def suggest_fix(status):

    fixes = {
        "CrashLoopBackOff":
            "Check application logs using kubectl logs",
        "ImagePullBackOff":
            "Verify container image name",
        "OOMKilled":
            "Increase memory limits"
    }

    return fixes.get(status, "Manual investigation required")
