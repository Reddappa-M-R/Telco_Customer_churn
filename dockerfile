FROM ubuntu:latest
COPY . /app
EXPOSE 8501
WORKDIR /app
RUN pip install -r requirements.txt

#ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit", "run", "App.py"]