from key import APIKEY
from typing import List, Dict, Callable
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)


class DialogueAgent:
    def __init__(self, user_type:str, system_message: SystemMessage, model: ChatOpenAI) -> None:
        self.user_type = user_type
        self.system_message = system_message
        self.model = model
        self.prefix = f"{self.user_type}: "
        self.message_history = None
        self.reset()

    def reset(self):
        self.message_history = []

    def send(self) -> str:
        message = self.model(
            [
                self.system_message,
                HumanMessage(content="\n".join(self.message_history + [self.prefix])),
            ]
        )
        return message.content

    def receive(self, user_type: str, message: str) -> None:
        self.message_history.append(f"{user_type}: {message}")


class Simulator:
    def __init__(
            self,
            agents: List[DialogueAgent],
            selection_function: Callable[[int, List[DialogueAgent]], int],
    ) -> None:
        self.agents = agents
        self._step = 0
        self.select_next_speaker = selection_function

    def reset(self):
        for agent in self.agents:
            agent.reset()

    def inject(self, name: str, message: str):
        for agent in self.agents:
            agent.receive(name, message)

        # increment time
        self._step += 1

    # def step(self) -> tuple[str, str]:
    #     # 1. choose the next speaker
    #     speaker_idx = self.select_next_speaker(self._step, self.agents)
    #     speaker = self.agents[speaker_idx]
    #
    #     # 2. next speaker sends message
    #     message = speaker.send()
    #
    #     # 3. everyone receives message
    #     for receiver in self.agents:
    #         receiver.receive(speaker.user_type, message)
    #
    #     # 4. increment time
    #     self._step += 1
    #
    #     return speaker.user_type, message