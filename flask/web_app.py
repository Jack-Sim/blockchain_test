from app import app, db
from app.models import User
from block_class import Block, Chain

chain = new Chain(3,"a")
print(chain)
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
