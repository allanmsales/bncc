from entity.open_ai import OpenAI

def rag_pipeline(question):
    open_ai = OpenAI()
    return open_ai.get_answer(question)