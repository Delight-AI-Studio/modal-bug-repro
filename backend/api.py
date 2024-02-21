from modal import Mount, asgi_app

from .common import api_image, stub

# from .worker import important_function # noqa F401

@stub.function(
    image=api_image,
    mounts=[Mount.from_local_python_packages("backend.api_app")]
)
@asgi_app()
def app():
    from backend.api_app import api_app
    return api_app