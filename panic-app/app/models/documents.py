from umongo import Document, fields
from app import app

instance = app.config['LAZY_UMONGO']

@instance.register
class Posts(Document):
    # title, body, author, published, meta{ upvotes, favs },
    title = fields.StrField(required=True)
    body = fields.StrField()
    published = fields.BoolField(False)
    meta = fields.DictField()