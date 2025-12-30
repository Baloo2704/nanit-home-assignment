class MobileSession:
    """
    A mock session that simulates Appium driver behavior.
    """
    def __init__(self, platform, config):
        self.platform = platform.lower()
        self.config = config
        print(f"[{self.platform.upper()}] Mobile Session Created")

    def launch_app(self):
        print(f"[{self.platform.upper()}] Launching Nanit App...")

    def find_element(self, element_id):
        """
        Simulates finding an element.
        Returns a mock element (dict) if 'found', or raises an error in a real scenario.
        """
        print(f"[{self.platform.upper()}] Finding element: {element_id}")
        return {"id": element_id, "found": True}

    def click(self, element):
        e_id = element.get('id', 'unknown')
        print(f"[{self.platform.upper()}] Clicking: {e_id}")

    def send_keys(self, element, text):
        e_id = element.get('id', 'unknown')
        # Mask password for logging
        display_text = "*****" if "password" in e_id else text
        print(f"[{self.platform.upper()}] Typing '{display_text}' into {e_id}")
    
    def quit(self):
        print(f"[{self.platform.upper()}] Closing App.")