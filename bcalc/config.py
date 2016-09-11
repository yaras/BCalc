import os
import json

class Config():
    def __init__(self, path='config.json'):
        if not os.path.isabs(path) and not os.path.exists(path):
            venv = os.environ.get('VIRTUAL_ENV')

            if venv:
                path = os.path.join(venv, path)

        with open(path, encoding='utf8') as config:
            self.params = json.load(config)

    def override(self, configs):
        for cfg in configs:
            with open(cfg, encoding='utf8') as config:
                params = json.load(config)

                for pp in params:
                    self.params[pp] = params[pp]

    def getAll(self):
        return self.params

    def override_single(self, params):
        for (k, v) in [vv.split('=') for vv in params]:
            if k not in self:
                raise Exception('Nieznany parametr {}'.format(k))

            if isinstance(self[k], float):
                self[k] = float(v)
            else:
                self[k] = v

    def __contains__(self, key):
        return key in self.params

    def __getitem__(self, key):
        return self.params[key]

    def __setitem__(self, key, value):
        self.params[key] = value
