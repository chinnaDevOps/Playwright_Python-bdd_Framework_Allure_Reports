import json
import os


def load_environment():
    # Step 1: get absolute path of the project root
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Step 2: point to config/environment.json
    config_path = os.path.join(base_dir, "config", "environment.json")

    print("ENV FILE PATH:", config_path)  # debug output

    # Step 3: fail early if file is missing
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Environment file not found at: {config_path}")

    # Step 4: load the JSON file
    with open(config_path, "r") as f:
        return json.load(f)
