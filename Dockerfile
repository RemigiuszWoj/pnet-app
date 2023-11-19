FROM python:3.10
COPY ./net-app /app/net-app
WORKDIR /app
RUN pip3 install -r net-app/requirements.txt
EXPOSE 8889
CMD [ "./net-app/src/net_app.py" ]