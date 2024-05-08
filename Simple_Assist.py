# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:46:39 2024

@author: Dakota
"""

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


OPENAI_API_TOKEN = "API_Token_Redacted"

SLACK_BOT_TOKEN = "Bot_Token_Redacted"

SLACK_APP_TOKEN = "App_Token_Redacted"


llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, api_key=OPENAI_API_TOKEN),

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)
messages = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "Translate this sentence from English to French. I love programming."),
]

llm.invoke(messages)


app = App(token=SLACK_BOT_TOKEN)

@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    
    output=messages
    say(output)


