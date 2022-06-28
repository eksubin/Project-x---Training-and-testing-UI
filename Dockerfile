FROM alpine
FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install streamlit
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT [ "streamlit", "run", "UI.py"]