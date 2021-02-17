FROM python:3.7-slim

RUN mkdir /src
WORKDIR /src

RUN pip install jupyterlab
COPY requirements.txt /src
RUN pip install -r requirements.txt

RUN apt update && apt install curl -y && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt install nodejs -y && \
    jupyter labextension install jupyterlab-plotly

CMD ["jupyter-lab", "--no-browser", "--allow-root", "--ip", "0.0.0.0"]
