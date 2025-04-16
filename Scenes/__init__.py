# Scenes/__init__.py

import os
import importlib

# Load all the scene modules dynamically
scene_modules = {}

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith(".py") and filename != "__init__.py":
        scene_name = filename[:-3]  # Remove the '.py' extension
        scene_module = importlib.import_module(f"Scenes.{scene_name}")
        scene_modules[scene_name] = scene_module
