#lets create a database

from models import User,Document

users_db={
    "alice": User(username="alice", department="hr"),
    "bob": User(username="bob", department="engineering"),
    "carol": User(username="carol", department="finance")
}


# Mock documents
documents_db = [
    Document(id=1, title="HR Policy", content="Confidential HR docs", department="hr"),
    Document(id=2, title="Engineering Design", content="Tech specs", department="engineering"),
    Document(id=3, title="Financial Report", content="Money stuff", department="finance")
]