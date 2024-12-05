import subprocess
import time

def run_java_loop(iterations):
    java_command = [
        "java",
        "-cp",
        "../compiled",
        "Loop",
        str(iterations)
    ]
    start_time = time.time()
    result = subprocess.check_output(java_command, text=True).strip()
    runtime = time.time() - start_time
    return float(result), runtime
