from injector import singleton
from app.impl.blog_json_impl import BlogJsonImpl
from app.service.blog_service import BlogService

def configure(binder):
    """Configure dependency injection for the BlogService."""
    binder.bind(BlogService, to=BlogJsonImpl, scope=singleton)
