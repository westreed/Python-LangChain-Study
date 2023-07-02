import os
import sys
from typing import *

from langchain.memory import ConversationBufferMemory


class DataManager:
    def __init__(self):
        self.company = None
        self.job = None
        self.requirement = None
        self.coverletter = None

    def set_data(self, input_data: Dict):
        self.company = input_data["user_company"]
        self.job = input_data["user_job"]
        self.requirement = input_data["job_requirement"]
        self.coverletter = input_data["cover_letter"]

    def get_data(self) -> Dict:
        return {
            "company": self.company,
            "job": self.job,
            "requirement": self.requirement,
            "coverletter": self.coverletter
        }


class MemoryManager:
    memory: ConversationBufferMemory

    def __init__(self):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    def get_memory(self) -> ConversationBufferMemory:
        return self.memory


class KeyManager:
    def __init__(self):
        self.openai_api_key = None
        self.serpapi_api_key = None
        if sys.platform == 'darwin':
            # MacOS
            self.openai_api_key = os.environ["OPENAI_API_KEY"]
            self.serpapi_api_key = os.environ["SERPAPI_API_KEY"]
        elif sys.platform == 'win32':
            # Windows
            self.openai_api_key = os.getenv("OPENAI_API_KEY")
            self.serpapi_api_key = os.getenv("SERPAPI_API_KEY")


class QuestionManager:
    def __init__(self, question_list: List):
        self.question = [] + question_list
        self.count = -1

    def get_question(self):
        self.count += 1
        return self.question[self.count]

    def ask_question_count(self):
        return self.count+1
    