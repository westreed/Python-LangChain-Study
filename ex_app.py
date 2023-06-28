# from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain import LLMChain, PromptTemplate, ConversationChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain.memory import ConversationBufferMemory

from key import APIKEY
from typing import List, Dict, Callable, Any, Union
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage, LLMResult, AgentAction, AgentFinish,
)

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


class StreamingStdOutCallbackHandler(BaseCallbackHandler):
    """Callback handler for streaming. Only works with LLMs that support streaming."""

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""

    def on_llm_new_token(self, token: str, **kwargs: Any) -> str:
        """Run on new LLM token. Only available when streaming is enabled."""
        print(token, end="")
        return token

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        print()

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when LLM errors."""


human_template = "{text}"

KEY = APIKEY()
memory = ConversationBufferMemory(return_messages=True)
chat = ChatOpenAI(openai_api_key=KEY.openai_api_key, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
chain = ConversationChain(llm=chat, memory=memory)


speech_list = [
    "당신은 면접관입니다. 지금부터, 회사인재를 뽑기 위한 면접관으로서 말투와 사고를 가져야 합니다. 개발자 직군과 관련해서 면접질문을 3개 생성해주세요.",
    "아까 생성했던 질문 3개 중 1개를 뽑아서 적어주세요.",
]
for speech in speech_list:
    chain.run(speech)

print(memory.load_memory_variables({}))