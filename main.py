import os
from langchain.llms import OpenAI

api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(openai_api_key=api_key, temperature=0.9)
print(llm.predict("화려한 색상의 양말을 만드는 회사의 이름을 추천해줘."))

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0)
chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
print(chat.predict("Translate this sentence from English to French. I love programming."))

from langchain.prompts import PromptTemplate

# prompt 텍스트에 포맷팅 기법 쓰는 방법
prompt = PromptTemplate.from_template("What is a {how} name for a company that makes {product}?")
formattingPrompt = prompt.format(how="good", product="colorful socks")
print(formattingPrompt)
print(llm.predict(formattingPrompt))

from langchain.chains import LLMChain

# 위에서 생성한 prompt와 llm을 chain으로 엮고, run에서 prompt인자를 넣을 수 있음.
chain = LLMChain(llm=llm, prompt=prompt)
chain.run(good="bad", product="colorful socks")