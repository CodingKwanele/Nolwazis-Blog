# Nolwazi Blog - Django HTMX Recipe App

## Vercel Deployment Guide

### 1. Environment Variables (How to deploy env)
Vercel reads env vars from dashboard, not .env file.

1. Go to [vercel.com](https://vercel.com) > New Project > Import Git repo (`nolwazi_blog/` contents).
2. **Settings > Environment Variables** - Add:
   ```
   DJANGO_SECRET_KEY=your-super-secret-key (python -c 'import secrets; print(secrets.token_urlsafe(50))')
   DJANGO_ALLOWED_HOSTS=your-app.vercel.app,.vercel.app
   DATABASE_URL=postgresql://... (create Vercel Postgres db, copy URL)
   DEBUG=false  # true for testing
   ```
3. Redeploy.

**See `.env.example` for template.** Never commit `.env`.

### 2. Local Testing
```
cd nolwazi_blog
python -m venv venv
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Load fixtures: `python manage.py loaddata recipes/fixtures/sample_recipes.json`

### 3. Vercel Specifics
- **Procfile + vercel.json**: Handles Python/Django.
- **PostgreSQL**: Create free db at vercel.com/storage, set DATABASE_URL.
- Auto-deploys on git push.

### 4. Post-Deploy
- Run migrations via Vercel Functions or shell: `python manage.py migrate`.
- Create superuser if needed.
- Visit `/admin` or `/` for recipes.

## Features
- Recipe CRUD, search, auth (HTMX-powered).
- Media/static served via WhiteNoise.

Built with Django 5.1 + HTMX.
