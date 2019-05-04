mkdir -p /app/logs /app/web/api/programme_tv
python scrapper_tv.py
gunicorn server_api.py:app
