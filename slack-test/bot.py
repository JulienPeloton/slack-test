import slack
import os

class Bot():
    def __init__(self, api_token):
        """
        """
        self.api_token = api_token
        self.client = slack.WebClient(token=api_token)

    def test_connection(self):
        """
        """
        self.client.auth_test()

    def send_message(self, channel_id, message):
        """
        """
        response = self.client.chat_postMessage(
            channel=channel_id, text=message, as_user="false",
            username="travisci", icon_emoji=":travisci:")

        return response


if __name__ == "__main__":
    api_token = os.environ["SLACK_API_TOKEN"]
    bot = Bot(api_token)

    print('testing connection')
    bot.test_connection()

    print('sending message')
    bot.send_message("fink-test-streamout", "Hi from inside the CI!")
