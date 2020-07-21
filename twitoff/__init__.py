#!/usr/bin/env Python
"""
Entry point from the TwitOff Flask web application
"""
# Local imports
from .app import create_app

APP = create_app()
