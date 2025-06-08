# vercel_wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Set the settings module – update 'myproject.settings' to your project's settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()

def handler(request, response):
    # Vercel’s Python runtime expects a function named "handler"
    # You can use a WSGI adapter to bridge to your Django app.
    from werkzeug.wrappers import Request, Response
    # Convert the incoming request into a WSGI environment and call the WSGI app.
    # For production deployment, consider using an adapter like 'werkzeug.wsgi.DispatcherMiddleware' or a custom adapter.
    environ = request.environ
    response_data = []
    def start_response(status, headers):
        response.status_code = int(status.split(" ")[0])
        for header in headers:
            response.headers.add(*header)
        return response_data.append

    result = application(environ, start_response)
    response.send("".join(result))
