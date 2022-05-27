FROM python:3-alpine
RUN pip install flask
COPY *.* /*.*
CMD ["python","MainGame.py"]
