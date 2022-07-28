import estoult
import yaml
from pydantic import BaseModel, Field

db = estoult.SQLiteDatabase(database='/home/arnar/Documents/notes/.zk/notebook.db')

class NoteSchema(db.Schema):
    __tablename__ = "notes"

    id = estoult.Field(int, primary_key=True)
    title = estoult.Field(str)
    path = estoult.Field(str)
    raw_content = estoult.Field(str)

class Note(BaseModel):
    id: int
    title: str
    path: str
    raw: str = Field(alias="raw_content")


notes = (
    estoult.Query(NoteSchema)
    .select("id", "title", "path", "raw_content")
    .execute()
)

ns = []
for n in notes:
    ns.append(Note(**n).dict())

print(yaml.dump(ns))
