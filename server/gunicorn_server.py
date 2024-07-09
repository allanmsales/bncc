import gunicorn.app.base as gunicorn_base
import multiprocessing


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class GunicornServer(gunicorn_base.BaseApplication):
    
    def init(self, parser, opts, args):
        pass

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()
    
    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)
    
    def load(self):
        return self.application
