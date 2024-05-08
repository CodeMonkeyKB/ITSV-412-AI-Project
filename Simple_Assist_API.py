# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:05:41 2024

@author: Dakota
"""

import os
import slack
import openai
import slack_sdk

# Set your Slack bot token and OpenAI API token
slack_bot_token = "Slack_Token_Redacted"
openai_token = "API_Token_Redacted"
slack_app_token = "App_Token_Redacted"



# Initialize the Slack client for both the app and bot
app_client = slack.WebClient(token=slack_app_token)
bot_client = slack.WebClient(token=slack_bot_token)

# Initialize the OpenAI API client
openai.api_key = openai_token

# Function to generate response using OpenAI API
def generate_response(message):
    response = openai.Completion.create(
        engine="davinci",  # You can change the engine according to your preference
        prompt=message,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to handle messages from Slack
def handle_message(message):
    response = generate_response(message)
    return response

# Function to send message to Slack
def send_message(channel, message):
    bot_client.chat_postMessage(channel=channel, text=message)

# Start the Slackbot
if __name__ == "__main__":
    # Establish connection with Slack
    rtm_client = slack.RTMClient(token=slack_bot_token)

    # Event handler for message events
    @slack.RTMClient.run_on(event='message')
    def handle_message(**payload):
        data = payload['data']
        if 'text' in data:
            channel_id = data['channel']
            user_id = data['user']
            text = data['text']
            response = handle_message(text)
            send_message(channel_id, response)

    # Start the Slack RTM client
    rtm_client.start()