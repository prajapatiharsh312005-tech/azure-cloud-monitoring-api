from flask import Flask
import psutil
import time

app = Flask(__name__)

START_TIME = time.time()

# Monitoring thresholds
CPU_WARNING = 70
CPU_CRITICAL = 90

MEMORY_WARNING = 70
MEMORY_CRITICAL = 90


@app.route("/")
def home():
    return "Cloud Monitoring API is running on Azure!"


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "azure-cloud-monitoring-api"
    }, 200


@app.route("/status")
def status():
    return {
        "service": "azure-cloud-monitoring-api",
        "status": "running",
        "environment": "Azure App Service"
    }, 200


@app.route("/metrics")
def metrics():

    cpu_percent = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()

    memory_percent = memory.percent

    uptime_seconds = int(time.time() - START_TIME)

    # Determine CPU status
    if cpu_percent >= CPU_CRITICAL:
        cpu_status = "critical"
    elif cpu_percent >= CPU_WARNING:
        cpu_status = "warning"
    else:
        cpu_status = "healthy"

    # Determine memory status
    if memory_percent >= MEMORY_CRITICAL:
        memory_status = "critical"
    elif memory_percent >= MEMORY_WARNING:
        memory_status = "warning"
    else:
        memory_status = "healthy"

    # Determine overall status
    if "critical" in [cpu_status, memory_status]:
        overall_status = "critical"
    elif "warning" in [cpu_status, memory_status]:
        overall_status = "warning"
    else:
        overall_status = "healthy"

    return {
        "service": "azure-cloud-monitoring-api",
        "status": overall_status,

        "cpu": {
            "usage_percent": cpu_percent,
            "status": cpu_status,
            "warning_threshold": CPU_WARNING,
            "critical_threshold": CPU_CRITICAL
        },

        "memory": {
            "usage_percent": memory_percent,
            "status": memory_status,
            "warning_threshold": MEMORY_WARNING,
            "critical_threshold": MEMORY_CRITICAL
        },

        "memory_used_mb": round(memory.used / (1024 * 1024), 2),
        "memory_available_mb": round(memory.available / (1024 * 1024), 2),

        "uptime_seconds": uptime_seconds
    }, 200


if __name__ == "__main__":
    app.run()