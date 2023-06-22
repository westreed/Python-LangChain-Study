import os, sys
from s1_llm_predict import init as s1_init
from s2_chat_predict import init as s2_init
from s3_llm_prompts_format import init as s3_init
from s4_llm_chain import init as s4_init
from s5_agent import init as s5_init
from s6_memory import init as s6_init


def get_api_key():
    openai_api_key = None
    serpapi_api_key = None

    if sys.platform == 'darwin':
        # MacOS
        openai_api_key = os.environ["OPENAI_API_KEY"]
        serpapi_api_key = os.environ["SERPAPI_API_KEY"]
    elif sys.platform == 'win32':
        # Windows
        openai_api_key = os.getenv("OPENAI_API_KEY")
        serpapi_api_key = os.getenv("SERPAPI_API_KEY")

    return {"openai_api_key": openai_api_key, "serpapi_api_key": serpapi_api_key}


if __name__ == "__main__":
    key = get_api_key()
    # s1_init(key["openai_api_key"])
    # s2_init(key["openai_api_key"])
    # s3_init(key["openai_api_key"])
    # s4_init(key["openai_api_key"])
    # s5_init(key["openai_api_key"], key["serpapi_api_key"])
    s6_init(key["openai_api_key"])
