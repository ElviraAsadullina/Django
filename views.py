import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def home(request):
    html = """
    <html>
    <head>
    <title>Main page</title>
    </head>
    <body>
    <h2>Welcome to my Django site!</h2>
    <p>This is my first Django site</p>
    </body>
    </html>
    """

    logger.info(f'User {request.META["REMOTE_ADDR"]} visited Main page')
    return HttpResponse(html)


def about(request):
    html = """
    <html>
    <head>
    <title>About</title>
    </head>
    <body>
    <h2>About me</h2>
    <p>My name is Elvira and I am new in Web development</p>
    </body>
    </html>
    """

    logger.info(f'User {request.META["REMOTE_ADDR"]} visited About page')
    return HttpResponse(html)
