import config
from langchain_openai import ChatOpenAI

class OpenAI:
    def __init__(self):
        pass

    @staticmethod
    def get_answer(question):
        llm = ChatOpenAI(api_key=config.OPENAI_API_KEY)
        response = llm.invoke(question)
        return response.content