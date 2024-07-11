import os
import shutil
import config
import time
import tiktoken
import json
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory


class OpenAI:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.observability = []

    def load_pdf(self, file_path) -> None:
        if os.path.exists('emb') and os.path.isdir('emb'):
            shutil.rmtree('emb')
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()

        Chroma.from_documents(
            pages,
            embedding=self.embeddings,
            persist_directory="emb"
        )

    def get_answer(self, question, history):
        memory = ConversationBufferMemory()
        chat = ChatOpenAI(api_key=config.OPENAI_API_KEY)

        db = Chroma(
            persist_directory="emb",
            embedding_function=self.embeddings
            )

        retriever = db.as_retriever()

        chain = RetrievalQA.from_chain_type(
            llm=chat,
            retriever=retriever,
            chain_type="stuff",
            memory=memory
        )

        #Main process
        start_time = time.time()
        result = chain.run(question)
        end_time = time.time()
        processing_time = end_time - start_time
        
        memory.save_context({"input": question}, {"output": result})

        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

        prompt_tokens = len(enc.encode(question))
        completion_tokens = len(enc.encode(result))
        total_tokens = prompt_tokens + completion_tokens

        cost_per_prompt_token = 0.00000005
        cost_per_completion_token = 0.0000015

        total_cost = (prompt_tokens * cost_per_prompt_token) + (completion_tokens * cost_per_completion_token)

        observability = {
            'processing_time': processing_time,
            'total_tokens': total_tokens,
            'total_cost': total_cost
        }

        self.observability.append(observability)

        with open('observability.json', 'w') as json_file:
            json.dump(self.observability, json_file, indent=4)

        return result   
