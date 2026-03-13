# My Application Management System (MAMS)

I built this because I needed a lightweight, no-frills way to track installed apps, their metadata, and whether to email users about updates. It’s a simple CRUD backend—no UI, no auth, just a SQL-backed API.

Uses Python 3.7+, SQLAlchemy, and Flask-Script. Runs behind an existing proxy if needed.

## What it does

- **Stores app metadata:** app_id (primary key), email, company_name, install_count, last_updated  
- **Tracks email opt-in status** via a boolean `sendemail` flag per app  
- **Persists data in SQLite or PostgreSQL**—just set `DATABASE_URL`  
- **Scales fine for 5k–10k daily writes**; tested up to 20k rows with minimal caching

## Installation

```bash
git clone https://github.com/yourusername/MAMS.git
cd MAMS
pip install -r requirements.txt
python manage.py db init && python manage.py db migrate
python manage.py runserver
```

## API

See [API_DOCS.md](API_DOCS.md) for endpoints, request formats, and example cURLs.

## Contributing

Bugs or feature ideas? [Open an issue](https://github.com/yourusername/MAMS/issues).  
Want to patch something? Fork, branch, PR—keep tests passing.

## License

MIT. See [LICENSE](LICENSE).