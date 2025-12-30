import json
import os
from pathlib import Path

class ConfigProvider:
    @staticmethod
    def load_config(env_path: str) -> dict:
        """
        Loads the configuration JSON and applies environment variable overrides.
        """
        project_root = Path(__file__).parent.parent
        config_full_path = project_root / env_path

        if not config_full_path.exists():
            raise FileNotFoundError(f"Config file not found at: {config_full_path}")

        with open(config_full_path, 'r') as f:
            config = json.load(f)
        
        # --- CI/CD Overrides ---
        if os.getenv("NANIT_BASE_URL"):
            config["stream_server"]["base_url"] = os.getenv("NANIT_BASE_URL")
            
        if os.getenv("NANIT_USERNAME"):
            config["mobile"]["username"] = os.getenv("NANIT_USERNAME")
        
        if os.getenv("NANIT_PASSWORD"):
            config["mobile"]["password"] = os.getenv("NANIT_PASSWORD")
            
        return config