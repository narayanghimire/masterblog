class BlogPost:
    def __init__(self, id: int, author: str, title: str, content: str):
        """Initialize a BlogPost with an ID, author, title, and content."""
        self.id = id
        self.author = author
        self.title = title
        self.content = content

    def to_dict(self):
        """Convert the BlogPost object to a dictionary representation."""
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'content': self.content
        }
