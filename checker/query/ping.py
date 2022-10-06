
import subprocess


def check_host_responds_to_pings(hostname: str) -> bool:

    # Execute system ping
    process = subprocess.Popen(
        ["ping", "-c3", "-q", "-W1", hostname], stdout=subprocess.PIPE)

    # Check the return code of the ping command
    return process.wait() == 0
