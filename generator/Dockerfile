FROM python:3.11

WORKDIR /app

COPY utils /tmp/utils
RUN pip install /tmp/utils && \
    pip list | grep utils && \
    python3 -c "import utils; print('utils imported successfully')" || exit 1

COPY generator/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY generator/generator.py .

CMD ["python3", "generator.py"]