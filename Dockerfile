FROM python:3.8
RUN python -m pip install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt
WORKDIR /src
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
ENTRYPOINT ["python"]
CMD ["APIcode.py"]
