mkdir -p /app/logs /app/web/programme_tv
python scrapper_tv.py
gunicorn server_api.py:app