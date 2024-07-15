# python

This app is a wrapper that starts [python](https://www.python.org/) in a docker container.

To install using [docker app install](https://github.com/dahenito/docker).

```bash
docker app install https://github.com/dahenito/python.git
```

Your entire $HOME is mounted inside the container with the same layout so you can reference the files exactly the same way as if they were on the host.

As an example, this is how you could run your apps on the host.

```bash
python -m pip install -r requirements.txt
python -m pip install gunicorn
python -m gunicorn --bind=:8000 --log-level=info app:app
```

Additional docker build/run flags could be added with DOCKER_BUILD_FLAGS
and DOCKER_RUN_FLAGS environment variables.

```bash
export DOCKER_BUILD_FLAGS="--progress plain"
export DOCKER_RUN_FLAGS="--publish 8000:8000"
```
