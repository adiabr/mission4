FROM python:3-alpine
RUN pip install flask
COPY ["Scores.txt","*.py"]
CMD ["python","MainGame.py"]
