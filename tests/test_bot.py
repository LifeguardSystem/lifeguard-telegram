import unittest

from unittest.mock import patch, MagicMock
from lifeguard_telegram.bot import init_updater

MOCK_CONTEXT = {}


class BotTest(unittest.TestCase):
    @patch("lifeguard_telegram.bot.CONTEXT", MOCK_CONTEXT)
    @patch("lifeguard_telegram.bot.Updater")
    def test_init_updater(self, mock_updater):
        instance_updater = MagicMock(name="updater")
        mock_updater.return_value = instance_updater

        init_updater()

        mock_updater.assert_called_with("", use_context=True)
        MOCK_CONTEXT["updater"].start_polling.assert_called()
        MOCK_CONTEXT["updater"].idle.assert_called()
