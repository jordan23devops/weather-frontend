FROM docker-flask-redis-web:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .
# Expose port 5000 as required
EXPOSE 5000
CMD ["python", "app.py"]
