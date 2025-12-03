FROM python:3.11-slim

WORKDIR /app

# Install system libs needed by pandas/numpy
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 && \
    rm -rf /var/lib/apt/lists/*
COPY . /app
COPY model/logistic_regression_model.pkl /app/model/logistic_regression_model.pkl



RUN pip install --no-cache-dir -r requirements.txt

# Remove broken old streamlit executable
RUN rm -f /usr/local/bin/streamlit

# Create new working launcher for Streamlit
RUN echo '#!/bin/sh\npython3 -m streamlit "$@"' > /usr/local/bin/streamlit && chmod +x /usr/local/bin/streamlit

# ensure python can import model_lr package
ENV PYTHONPATH="/app"

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "\
    uvicorn main:app --host 0.0.0.0 --port 8000 & \
    streamlit run ui/frontend.py --server.address=0.0.0.0 --server.port=8501 \
"]

