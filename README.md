# Python Langchain Study

## Install

```commandline
pip install langchain
pip install openai                  // ChatGPT API
pip install google-search-results   // Google Search API
```

## Learning

1. 언어모델(LLMs)

텍스트 문자열을 입력하고, 텍스트 문자열을 출력하는 모델입니다.
LangChain 은 LLM 공급자가 아니며, 인터페이스만 제공합니다.  
`아마, 기본적으로 OpenAI의 GPT API를 똑같이 사용하지만 단순히 질의응답 형태로 쓸 수 있게 제공하는 것 같음.`

2. 채팅모델(Chat)

채팅 모델은 언어 모델의 변형으로, 내부적으로는 언어 모델을 사용하지만 노출되는 인터페이스는 약간 다릅니다.
현재는 System, Human, AI 3종류의 사용자를 지원합니다.

- System : AI에게 해야 할 일을 알려주는 배경 컨텍스트
- Human : 사용자 메세지
- AI : AI가 응답한 내용을 보여주는 상세 메세지


## ETC

PyCharm 커뮤니티버전에서 쥬피터 노트북을 쓰고 싶을 땐,
[링크](https://tariat.tistory.com/169) 참고하세요.