FROM python:3.7-slim

RUN mkdir /src

WORKDIR /src

RUN pip install jupyterlab

CMD ["jupyter-lab", "--no-browser", "--allow-root", "--ip", "0.0.0.0"]
