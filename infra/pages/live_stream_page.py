from infra.ui_map import UIMap
from infra.pages.base_page import BasePage

class LiveStreamPage(BasePage):
    def is_stream_visible(self):
        element = self._find(UIMap.LIVE_STREAM_CONTAINER)
        return element.get('found', False)