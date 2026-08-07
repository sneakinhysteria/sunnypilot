import os

from openpilot.common.api.base import BaseApi

# Konik Stable rather than comma connect: the device is a Konik A1 and the
# account lives on their backend. Still overridable by env var.
API_HOST = os.getenv('API_HOST', 'https://api.konik.ai/')


class CommaConnectApi(BaseApi):
  def __init__(self, dongle_id):
    super().__init__(dongle_id, API_HOST)
    self.user_agent = "openpilot-"
