from ..common import stub, worker_image

@stub.function(
    image=worker_image,
)
def important_function():
    return "important result"