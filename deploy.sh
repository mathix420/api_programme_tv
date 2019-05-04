mkdir -p /app/logs /app/web/api/programme_tv
python scrapper_tv.py
cd /app
gunicorn server_api.py:app
