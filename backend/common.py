from modal import Image, Stub

stub = Stub("modal-bug-repro")

api_image = Image.debian_slim().poetry_install_from_file("pyproject.toml", with_=["api"])

worker_image = Image.debian_slim().poetry_install_from_file("pyproject.toml", with_=["worker"])