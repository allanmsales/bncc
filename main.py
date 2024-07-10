from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.gunicorn_server import GunicornServer
from controller import agent

app = FastAPI(
    title="Retrieving Agent for BNCC",
    version="0.1",
    description="Agent to answer questions about BNCC."
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(agent.router)

if __name__ == '__main__':
    options = {
        'bind': '{}:{}'.format('0.0.0.0', '8080'),
        'workers': 1,
        'worker_class': 'uvicorn.workers.UvicornWorker',
        'timeout': 600
    }

    GunicornServer(app, options).run()
