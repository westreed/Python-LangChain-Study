import os
from s1_llm_predict import init as s1_init
from s2_chat_predict import init as s2_init
from s3_llm_prompts_format import init as s3_init
from s4_llm_chain import init as s4_init
from s5_agent import init as s5_init

if __name__ == "__main__":
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    SERPAPI_API_KEY = os.environ["SERPAPI_API_KEY"]
    # s1_init(OPENAI_API_KEY)
    # s2_init(OPENAI_API_KEY)
    # s3_init(OPENAI_API_KEY)
    # s4_init(OPENAI_API_KEY)
    s5_init(OPENAI_API_KEY, SERPAPI_API_KEY)