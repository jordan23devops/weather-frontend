FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .
# Expose port 5000 as required
EXPOSE 5000
CMD ["python", "app.py"]
