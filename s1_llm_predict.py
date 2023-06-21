from langchain.llms import OpenAI


def init(openai_api_key):
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
    print(llm.predict("화려한 색상의 양말을 만드는 회사의 이름을 추천해줘."))