# Chess Academy Payment System

A Django application for tracking monthly payments from parents of a chess academy.

## Quick Start

### Build and Run

```bash
cd chess_academy
docker-compose up --build
```

Wait for the build to complete and migrations to run.

### Create Admin User

```bash
docker-compose exec web python manage.py createsuperuser
```

### Access the App

- Website: http://localhost:8000
- Admin: http://localhost:8000/admin

## Usage

1. **Public Page**: Anyone can view payment status at the homepage
2. **Admin**: Login at `/admin/` to manage parents and mark payments
3. **Mark Paid**: Click "Mark Paid" button on a parent to record their payment
4. **Add Parents**: Use the admin panel or dashboard to add new parents

## Commands

```bash
# Start the app
docker-compose up

# Start in background
docker-compose up -d

# Stop the app
docker-compose down

# View logs
docker-compose logs -f

# Run management commands
docker-compose exec web python manage.py [command]

# Create sample data
docker-compose exec web python manage.py create_sample_data

# Database shell
docker-compose exec db psql -U postgres -d chess_academy
```

## Deployment

The app uses PostgreSQL which is production-ready. To deploy:

1. Set environment variables:
   - `DEBUG=0` (disable debug mode)
   - `SECRET_KEY` (generate a strong secret key)
   - `DATABASE_URL` (your production PostgreSQL URL)

2. Use a production WSGI server like Gunicorn instead of runserver

3. Set up proper static files serving

## Features

- PostgreSQL database (production-ready)
- Track monthly payments from parents
- Public payment status page
- Admin dashboard for managing payments
- Add/edit/delete parents
- Monthly payment statistics
- Responsive Tailwind CSS design
