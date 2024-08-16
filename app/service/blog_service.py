from abc import ABC, abstractmethod
from typing import List

from app.model.blog_post import BlogPost


class BlogService(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_posts(self) -> List[BlogPost]:
        """Load and return all blog posts."""
        pass

    @abstractmethod
    def save_posts(self, posts: List[BlogPost]) -> None:
        """Save the provided list of blog posts."""
        pass

    @abstractmethod
    def add_post(self, post: BlogPost) -> None:
        """Add a new blog post."""
        pass

    @abstractmethod
    def delete_post(self, post_id: int) -> None:
        """Delete the blog post with the given ID."""
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: int) -> BlogPost | None:
        """Retrieve a blog post by its ID."""
        pass

    @abstractmethod
    def update_post(self, post: BlogPost) -> None:
        """Update an existing blog post."""
        pass
