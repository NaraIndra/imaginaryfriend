FROM python:3.6
RUN mkdir /build
WORKDIR /build
ADD requirements.txt /build/
RUN pip install -r requirements.txt
ADD . /build/
EXPOSE 5000
