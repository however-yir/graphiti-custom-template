#!/usr/bin/env python3
"""
Main entry point for Graphiti Custom MCP Server

This is a backwards-compatible wrapper around the original graphiti_mcp_server.py
to maintain compatibility with existing deployment scripts and documentation.

Usage:
    python main.py [args...]

All arguments are passed through to the original server implementation.
"""

import sys
from pathlib import Path

# Add src directory to Python path for imports
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

# Add repository root to Python path for local graphiti_core imports
repo_root = Path(__file__).parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Import and run the original server
if __name__ == '__main__':
    from graphiti_mcp_server import main

    # Pass all command line arguments to the original main function
    main()
