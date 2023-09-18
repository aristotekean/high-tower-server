# 
FROM python:3.9

# 
WORKDIR /usr/src/app

# 
COPY ["requirements.txt", "."]

# 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 
COPY . /usr/src/app

#
EXPOSE 8000:8000

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
