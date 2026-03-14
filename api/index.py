from vercel_wsgi import handle_wsgi_app
from app import app

def handler(request, response):
    return handle_wsgi_app(app, request, response)
