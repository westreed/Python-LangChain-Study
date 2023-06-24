import os
import sys


class APIKEY:
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