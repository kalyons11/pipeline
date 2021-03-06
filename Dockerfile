FROM alpine:3.5
RUN apk add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY run.py /src
COPY buzz /src/buzz

# Setup env vars
ENV FOO BAR

CMD python /src/run.py