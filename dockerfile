FROM ubuntu:latest
COPY . /home/reddymr
EXPOSE 8501
WORKDIR /home/reddymr
RUN pip install -r requirements.txt

#ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit", "run", "App.py"]