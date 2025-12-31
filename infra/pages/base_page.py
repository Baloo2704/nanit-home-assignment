class BasePage:
    def __init__(self, session):
        self.session = session
        self.platform = session.platform

    def _find(self, element_map):
        element_id = element_map.get(self.platform)
        return self.session.find_element(element_id)

    def _click(self, element_map):
        element = self._find(element_map)
        self.session.click(element)

    def _type(self, element_map, text):
        element = self._find(element_map)
        self.session.send_keys(element, text)