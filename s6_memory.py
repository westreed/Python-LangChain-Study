from langchain import OpenAI, ConversationChain


def init(openai_api_key):
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
    conversation = ConversationChain(llm=llm, verbose=True)

    while True:
        human_input = input("할말을 작성하세요.\n")
        if human_input in ["exit", "c"]: break
        res = conversation.run(human_input)
        print(f"AI : {res}")
