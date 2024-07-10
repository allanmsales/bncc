from entity.open_ai import OpenAI


def rag_pipeline(question, history):
    open_ai = OpenAI()
    answer = open_ai.get_answer(question, history.history)
    history.add_to_history_agent(answer)
    return history.history