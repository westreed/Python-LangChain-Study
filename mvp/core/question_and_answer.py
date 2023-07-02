from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)

from mvp.data_manager import *
from custom_callback_handler import CustomCallbackHandler
from typing import *


def question_and_answer(
    data_manager: DataManager,
    memory_manager: MemoryManager,
    key_manager: KeyManager,
    question_manager: QuestionManager
):
    pass
