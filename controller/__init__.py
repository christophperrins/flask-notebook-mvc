from app import app
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith("_") and not x.startswith("query") and not x.startswith("meta")]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) #dict, tuple, list, string, int
                    fields[field] = data
                except TypeError:
                    pass
        return fields

from controller import note_controller, notebook_controller