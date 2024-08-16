from uuid import uuid4


class BlogPost:
    def __init__(self, id: int, author: str, title: str, content: str):
        self.id = id
        self.author = author
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'content': self.content
        }