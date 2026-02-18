"""Orchestrator-only tools: stamp and finalize_report."""
from __future__ import annotations

from typing import Any, Dict


def orchestrator_stamp(run_id: str) -> Dict[str, Any]:
    """A tiny tool to prove orchestrator also calls a tool."""
    return {"status": "ok", "run_id": run_id}


def finalize_report(
    run_id: str,
    math_result: Dict[str, Any],
    text_result: Dict[str, Any],
) -> Dict[str, Any]:
    """Merge sub-agent outputs into one report. Called by orchestrator."""
    return {
        "status": "ok",
        "run_id": run_id,
        "math": math_result,
        "text": text_result,
    }
