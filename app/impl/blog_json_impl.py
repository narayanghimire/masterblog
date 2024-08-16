import json
import os
from typing import List

from app.model.blog_post import BlogPost
from app.service.blog_service import BlogService


class BlogJsonImpl(BlogService):
    def __init__(self):
        super().__init__()
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        data_file = os.path.join(project_root, 'static/posts.json')
        self.file_path = data_file

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file at {self.file_path} does not exist")

    def load_posts(self) -> List[BlogPost]:
        try:
            with open(self.file_path, 'r') as file:
                posts_data = json.load(file)
                return [BlogPost(**post) for post in posts_data]
        except FileNotFoundError:
            return []

    def save_posts(self, posts: List[BlogPost]) -> None:
        with open(self.file_path, 'w') as file:
            json.dump([post.to_dict() for post in posts], file)

    def add_post(self, post: BlogPost) -> None:
        posts = self.load_posts()
        posts.append(post)
        self.save_posts(posts)

    def delete_post(self, post_id: int) -> None:
        posts = self.load_posts()
        updated_posts = [post for post in posts if post.id != post_id]
        self.save_posts(updated_posts)

    def get_post_by_id(self, post_id: int) -> BlogPost | None:
        posts = self.load_posts()
        for post in posts:
            if post.id == post_id:
                return post
        return None

    def update_post(self, updated_post: BlogPost) -> None:
        posts = self.load_posts()
        for i, post in enumerate(posts):
            if post.id == updated_post.id:
                posts[i] = updated_post
                self.save_posts(posts)
                return