from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


def init(openai_api_key):
    chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
    print(chat.predict("Translate this sentence from English to French. I love programming."))