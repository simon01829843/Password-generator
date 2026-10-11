# Base44 Dev Environment

## Project Overview
This is a Python password generator. The original `main.py` is a CLI script that prompts for a password length and prints a random password. To make it viewable in the browser preview, `app.py` wraps the same generation logic in a Flask web app served on port 3000.

## Running the App
```bash
docker compose -f docker-compose.base44.yml up -d --build
```
The app is served at http://localhost:3000.

## Architecture
- `main.py` — original CLI password generator (unchanged)
- `app.py` — Flask web app reusing the same password character set, served on port 3000 with debug auto-reload
- `templates/index.html` — single-page UI with a length input and generate button
- `requirements.txt` — Flask dependency

## Notes
- No external credentials or secrets are needed.
- Flask debug mode provides live reload on file changes.
- Dependencies are installed on container startup from `requirements.txt`.
