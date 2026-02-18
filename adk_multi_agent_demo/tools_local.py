from __future__ import annotations

import math
import re
from typing import Dict, Any


def orchestrator_stamp(run_id: str) -> Dict[str, Any]:
    """A tiny tool to prove orchestrator also calls a tool."""
    return {"status": "ok", "run_id": run_id}


_ALLOWED = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "pow": pow,
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e,
}

_BAD = re.compile(r"(__|import|exec|eval|open|os\.|sys\.|subprocess|socket|pickle)", re.I)


def safe_calc(expr: str) -> Dict[str, Any]:
    """
    Safe-ish calculator tool for demo.
    Supports simple math expression, e.g. "((3+5)*2)/4", "sqrt(16)+log10(100)".
    """
    if not expr or len(expr) > 200:
        return {"status": "error", "error": "expr too long/empty"}

    if _BAD.search(expr):
        return {"status": "error", "error": "disallowed token"}

    try:
        # Evaluate with restricted globals/locals
        val = eval(expr, {"__builtins__": {}}, _ALLOWED)  # noqa: S307 (demo)
        return {"status": "ok", "expression": expr, "result": val}
    except Exception as e:
        return {"status": "error", "error": str(e)}
