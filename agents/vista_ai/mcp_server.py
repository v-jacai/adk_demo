"""MCP server (stdio): entry point for ADK subprocess. Do not print to stdout."""
from __future__ import annotations

import re
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo-text-mcp")


@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the input text."""
    return text[::-1]


@mcp.tool()
def slugify(text: str) -> str:
    """Make a simple URL-friendly slug."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
