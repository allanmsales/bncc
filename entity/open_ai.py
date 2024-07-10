import config
from langchain_openai import ChatOpenAI

class OpenAI:
    def __init__(self):
        pass

    @staticmethod
    def get_answer(question, history):
        llm = ChatOpenAI(api_key=config.OPENAI_API_KEY)
        prompt = f'Levando em consideração esse histórico de conversa anterior: {history}, responda a seguinte pergunta: {question}'
        response = llm.invoke(prompt)
        return response.content