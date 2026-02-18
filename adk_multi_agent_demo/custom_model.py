"""
Custom model using google-genai 1.63.0, integrated with Google ADK.

Use either:
- A base Gemini model with optional config (get_custom_model_for_adk), or
- A tuned model created via create_custom_tuned_model (run scripts/create_custom_tuned_model.py).
"""
from __future__ import annotations

import os
from typing import Optional

from google.adk.models.google_llm import Gemini
from google.genai import types


# Default base model when no tuned model name is set
DEFAULT_BASE_MODEL = "gemini-2.5-flash"


def get_custom_model_for_adk(
    model_name: Optional[str] = None,
    *,
    retry_options: Optional[types.HttpRetryOptions] = None,
) -> Gemini:
    """
    Build an ADK Gemini model backed by google-genai 1.63.0.

    Use this as the `model` argument for LlmAgent. ADK uses the same
    google-genai client (version pinned in requirements.txt).

    Args:
        model_name: Gemini model ID (e.g. "gemini-2.5-flash") or a tuned
            model name (e.g. "tunedModels/your-model-id"). If None, uses
            DEFAULT_BASE_MODEL.
        retry_options: Optional HTTP retry options for the genai client.

    Returns:
        Gemini instance to pass to LlmAgent(model=...).
    """
    name = model_name or os.environ.get("ADK_CUSTOM_MODEL", DEFAULT_BASE_MODEL)
    return Gemini(
        model=name,
        retry_options=retry_options or types.HttpRetryOptions(
            initial_delay=1.0,
            attempts=3,
        ),
    )
