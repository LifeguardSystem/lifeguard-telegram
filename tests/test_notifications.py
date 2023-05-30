import unittest
from unittest.mock import patch, MagicMock, call

from datetime import datetime

MOCK_TELEPOT = MagicMock(name="telepot")

from lifeguard_telegram.notifications import TelegramNotificationBase


class TelegramNotificationBaseTest(unittest.TestCase):
    def setUp(self):
        self.notification = TelegramNotificationBase()
        self.mock_bot = MagicMock(name="bot")
        MOCK_TELEPOT.Bot.return_value = self.mock_bot

    def test_get_name(self):
        self.assertEqual(self.notification.name, "telegram")

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_send_single_message(self):
        self.notification.send_single_message("content", {})
        self.mock_bot.sendMessage.assert_called_with(
            "", text="content", parse_mode="Markdown"
        )

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_send_multiple_single_message(self):
        self.notification.send_single_message(["line1", "line2"], {})

        self.mock_bot.sendMessage.assert_has_calls(
            [
                call("", text="line1", parse_mode="Markdown"),
                call("", text="line2", parse_mode="Markdown"),
            ]
        )

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_init_thread(self):
        self.notification.init_thread("content", {})

        self.mock_bot.sendMessage.assert_called_with(
            "", text="content", parse_mode="Markdown"
        )

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    @patch("lifeguard_telegram.notifications.datetime")
    def test_init_thread_with_multiples_messages(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 10, 11)

        threads = self.notification.init_thread(["line1", "line2"], {})

        self.mock_bot.sendMessage.assert_has_calls(
            [
                call("", text="line1", parse_mode="Markdown"),
                call("", text="line2", parse_mode="Markdown"),
            ]
        )

        self.assertEqual(threads, ["202210110000"])

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_update_thread(self):
        self.notification.update_thread(["thread"], "content", {})

        self.mock_bot.sendMessage.assert_called_with(
            "", text="content", parse_mode="Markdown"
        )

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_close_thread(self):
        self.notification.close_thread(["thread"], "content", {})

        self.mock_bot.sendMessage.assert_called_with(
            "", text="content", parse_mode="Markdown"
        )

    @patch("lifeguard_telegram.notifications.telepot", MOCK_TELEPOT)
    def test_error_on_send_message(self):
        self.mock_bot.sendMessage.side_effect = [Exception("error"), None]
        self.notification.close_thread(["thread"], "content", {})

        self.mock_bot.sendMessage.assert_called_with(
            "", text="there was an error sending the message"
        )
