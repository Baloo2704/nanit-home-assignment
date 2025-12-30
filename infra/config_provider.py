import json
from pathlib import Path

class ConfigProvider:
    @staticmethod
    def load_config(env_path: str) -> dict:
        """
        Loads the configuration JSON from the specified relative path.
        Args:
            env_path: Relative path from the config directory (e.g., "config.json")
        """
        # Calculate absolute path relative to the project root
        # Assuming config files located in ./infra/config/
        config_dir = Path(__file__).parent / "config"
        config_full_path = config_dir / env_path

        if not config_full_path.exists():
            raise FileNotFoundError(f"Config file not found at: {config_full_path}")

        with open(config_full_path, 'r') as f:
            return json.load(f)