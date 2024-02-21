# Modal Bug Repro

This repro shows a bug I encountered while trying to invoke a modal function from inside a fastapi endpoint.

### Repro steps

1. install poetry
2. run `poetry run modal serve backend.api`
3. make a POST request to the test endpoint (be sure to replace <subdomain> with whatever subdomain you have): `curl -X POST -H "Content-Type: application/json" https://<subdomain>.modal.run/`

The request will 500, and you should see the following error:

```
modal.exception.ExecutionError: Object has not been hydrated and doesn't support lazy hydration. This might happen if an object is defined on a different stub, or if it's on the same stub but it didn't get created because it wasn't defined in global scope.
```

### Fix

1. uncomment line 5 of backend/api.py
2. go through the repro steps above

Now, the request should 200 and you should receive the following response:

```
{"message":"important result"}
```

### My comments / confusion

I may just be misunderstanding how imports / mounts work in modal, and I'm relatively new to python in general (more used to Typescript).

But I found it pretty confusing that doing `from .worker import important_function` doesn't work when I only do it in the file where
I actually use the function, but then adding an unused import at the top of the backend/api.py file (or in `backend/__init__.py`) fixes
this issue.

More broadly, I'm a bit unsure why either approach would work, to be honest. I'm only mounting `backend.api_app` to the api function, so
I didn't really expect anything from `backend/worker` to be available in that context and that I'd have to use `modal.Function.lookup`,
but that didn't seem to work either.

I'm _guessing_ that this all has to do with `modal serve` only building the images that it sees at the top-level, and so the worker image
isn't getting built?
