FROM python:3.5
ADD requirements.txt /src/
RUN cd /src && pip install -r requirements.txt
ADD . /src/
RUN cd /src && pip install .
ADD ./tests.py /test/
WORKDIR /test
