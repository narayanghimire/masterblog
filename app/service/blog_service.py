from abc import ABC, abstractmethod
from typing import List

from app.model.blog_post import BlogPost


class BlogService(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def load_posts(self) -> List[BlogPost]:
        pass

    @abstractmethod
    def save_posts(self, posts: List[BlogPost]) -> None:
        pass

    @abstractmethod
    def add_post(self, post: BlogPost) -> None:
        pass

    @abstractmethod
    def delete_post(self, post_id: int) -> None:
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: int) -> BlogPost | None:
        pass

    @abstractmethod
    def update_post(self, post: BlogPost) -> None:
        pass
