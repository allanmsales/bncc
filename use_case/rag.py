from entity.open_ai import OpenAI

open_ai = OpenAI()
open_ai.load_pdf('bncc.pdf')

def rag_pipeline(question, history):
    answer = open_ai.get_answer(question, history.history)
    history.add_to_history_agent(answer)
    response = history.history_zip()
    return response