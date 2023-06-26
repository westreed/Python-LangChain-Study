from key import APIKEY
from typing import List, Dict, Callable
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)


class DialogueAgent:
    """docs
    가장 최하위 대화모델로, Simulator 클래스에서 inject를 통해, 모든 agent에
    대화를 공유한다. 역할과 시스템 메시지를 분리하기 위해, 이런 방식이 채택됨.
    """
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

    def step(self) -> tuple[str, str]:
        # 1. choose the next speaker
        speaker_idx = self._step % 2
        speaker = self.agents[speaker_idx]

        # 2. next speaker sends message
        message = speaker.send()

        # 3. everyone receives message
        for receiver in  self.agents:
            receiver.receive(speaker.user_type, message)

        # 4. next step
        self._step += 1

        return speaker.user_type, message

"""
1. 모델은 Input을 통해, 질문을 생성해야 한다.
2. 모델은 질문과 답변을 제공받고, 평가를 해야한다.
3. 기준에 따라, 위에서 제공받은 데이터를 기반으로 꼬리질문을 1개 생성해야한다.


역할이 2개이상 필요한가?
"""