"""Central config: env and tuning constants. Used by services and pipeline (future)."""
from __future__ import annotations

import os
from pathlib import Path

# Env loading (optional)
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

# -----------------------------------------------------------------------------
# LLM / Embedding
# -----------------------------------------------------------------------------
DEFAULT_MODEL = os.environ.get("VISTA_LLM_MODEL", "gemini-2.5-flash")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")

# -----------------------------------------------------------------------------
# Pipeline / SQL / Config (placeholders for future Vista pipeline)
# -----------------------------------------------------------------------------
# DEFAULT_LIMIT = int(os.environ.get("VISTA_DEFAULT_LIMIT", "200"))
# MAX_LIMIT = int(os.environ.get("VISTA_MAX_LIMIT", "2000"))
# MAX_SQL_ATTEMPTS = int(os.environ.get("VISTA_MAX_SQL_ATTEMPTS", "10"))
# MAX_CONFIG_ATTEMPTS = int(os.environ.get("VISTA_MAX_CONFIG_ATTEMPTS", "3"))

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent
SCHEMA_CATALOG_DIR = REPO_ROOT / "schema_catalog"
VISTA_SCHEMA_PATH = REPO_ROOT / "schema_cache" / "vista_schema.json"
