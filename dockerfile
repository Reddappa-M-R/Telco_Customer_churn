FROM ubuntu:latest
COPY . /app
EXPOSE 8502
WORKDIR /app
RUN pip3 install -r requirements.txt

#ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit", "run", "App.py"]