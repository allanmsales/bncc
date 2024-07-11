# BNCC Agent
Retrieving Agent for Bncc Information

# Installation
Ubuntu 22.04
Python 3.10

* $ python3 -m venv env
* $ source env/bin/activate
* $ pip install -r requirements.txt
* $ python3 main.py

* Include the source file using the name bncc.pdf in the root of the project
* Include a .env file in project root with the following info:

OPENAI_API_KEY=[your_openai_api_key]

Access this url to use the chat:
http://localhost:8080/agent/


Access this url to see the summary of utilization:
http://localhost:8080/agent/observability


# How it works

* At the first time that the project runs it will read the PDF file and split it into chunks.Each page is one chunk.
* For each chunk we will generate the embeddings vector using Openai Embeddings and store the chunk and the embeddings in a vector database (chromadb). This process could take some time, after that the server will launch and the endpoint will be available.
* When the endpoint is called, we create an embeddings for the question and look for the most similar embeddings vectors in the vector dataset.
* We use Langchain to include the user's question and the most relevant chunks into the prompt and send it to Openai.
* We return the answer to the user. 

# Docs

* The documentation is available at:

http://localhost:8080/docs


