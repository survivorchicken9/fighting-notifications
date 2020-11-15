import uuid
from dataclasses import dataclass, field
from datetime import date
from typing import Dict
from common.database import Database


@dataclass(eq=False)
class Friend:
    collection: str = field(init=False, default="friends")
    name: str
    end_date: date
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {"_id": self._id, "name": self.name, "end_date": self.end_date}

    def save_to_mongo(self):
        Database.insert(self.collection, self.json())
