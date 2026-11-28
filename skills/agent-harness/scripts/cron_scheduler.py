#!/usr/bin/env python3
"""
Local Cron Job Runner for Agent Harness.
Executes a recurring command or prompt N times at a given interval and persists
every output to a log file (fixing silent terminal UI drop-offs).
"""

import argparse
import datetime
import json
import subprocess
import time
from pathlib import Path


def run_cron(job_name: str, command: str, interval: float, max_runs: int, log_file: Path) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    for idx in range(1, max_runs + 1):
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        proc = subprocess.run(command, shell=True, capture_output=True, text=True)
        record = {
            "job": job_name,
            "run_number": idx,
            "max_runs": max_runs,
            "timestamp": ts,
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
        with log_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"[{job_name}] Run {idx}/{max_runs} -> exit={proc.returncode} | {record['stdout']}")
        if idx < max_runs:
            time.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reliable local cron runner with persistent JSONL logging")
    parser.add_argument("--name", required=True, help="Job name")
    parser.add_argument("--cmd", required=True, help="Shell command to execute each run")
    parser.add_argument("--interval", type=float, default=60.0, help="Seconds between runs")
    parser.add_argument("--max-runs", type=int, default=10, help="Total number of runs")
    parser.add_argument("--log", default=".hermes/logs/cron_jobs.jsonl", help="Persistent JSONL log path")
    args = parser.parse_args()
    run_cron(args.name, args.cmd, args.interval, args.max_runs, Path(args.log))


if __name__ == "__main__":
    main()
