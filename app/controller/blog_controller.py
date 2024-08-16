from uuid import uuid4

from flask import Blueprint, render_template, request, redirect, url_for
from injector import inject

from app.model.blog_post import BlogPost
from app.service.blog_service import BlogService

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
@inject
def index(blog: BlogService):
    posts = blog.load_posts()
    return render_template('index.html', posts=posts)

@blog_bp.route('/add', methods=['GET', 'POST'])
@inject
def add(blog: BlogService):
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        if title and author and content:
            blog_post = BlogPost(uuid4().int, title=title, author=author, content=content)
            blog.add_post(blog_post)
            return redirect(url_for('blog.index'))

    return render_template('add.html')

@blog_bp.route('/delete/<int:post_id>')
@inject
def delete(post_id: int, blog: BlogService):
    blog.delete_post(post_id)
    return redirect(url_for('blog.index'))


@blog_bp.route('/update/<int:post_id>', methods=['GET', 'POST'])
@inject
def update(blog: BlogService, post_id: int):
    post = blog.get_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        if title and author and content:
            updated_post = BlogPost(id=post_id, title=title, author=author, content=content)
            blog.update_post(updated_post)
            return redirect(url_for('blog.index'))

    return render_template('update.html', post=post)