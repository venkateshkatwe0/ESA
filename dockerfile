FROM python:3.13.9
WORKDIR /app
COPY . .
CMD [ "python","average_marks.py" ]