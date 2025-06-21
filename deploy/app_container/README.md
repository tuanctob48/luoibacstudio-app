# Wagtail with Supabase PostgreSQL Docker Setup

This setup creates a Wagtail CMS application connected to your existing Supabase PostgreSQL database using Docker.

## Quick Start

### Using Docker Compose (Recommended)

1. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your Supabase credentials
   ```

2. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Wagtail Admin: http://localhost:8000/admin/
   - Frontend: http://localhost:8000/
   - Default admin credentials: `admin/admin`

### Using Docker Only

1. **Build and run the Wagtail app:**
   ```bash
   docker build -t luoibac-studio .
   docker run -d \
     --name wagtail-app \
     -e POSTGRES_DB=postgres \
     -e POSTGRES_USER=postgres \
     -e POSTGRES_PASSWORD=your-supabase-password \
     -e POSTGRES_HOST=db.your-project-ref.supabase.co \
     -e POSTGRES_PORT=5432 \
     -e SECRET_KEY=your-secret-key \
     -p 8000:8000 \
     luoibac-studio
   ```

## Environment Variables

The application uses the following environment variables:

- `SUPABASE_DB_HOST`: Your Supabase database host (e.g., `db.your-project-ref.supabase.co`)
- `SUPABASE_DB_PASSWORD`: Your Supabase database password
- `POSTGRES_DB`: Database name (default: `postgres` for Supabase)
- `POSTGRES_USER`: Database user (default: `postgres` for Supabase)
- `POSTGRES_PASSWORD`: Database password (from Supabase)
- `POSTGRES_HOST`: Database host (from Supabase)
- `POSTGRES_PORT`: Database port (default: `5432`)
- `SECRET_KEY`: Django secret key (required for production)
- `DJANGO_SETTINGS_MODULE`: Django settings module (default: `luoibacstudio.settings.production`)
- `DEBUG`: Set to 'True' for development mode (default: 'False' for production)

## Supabase Configuration

To get your Supabase database credentials:

1. Go to your Supabase project dashboard
2. Navigate to Settings > Database
3. Copy the connection information:
   - Host: `db.your-project-ref.supabase.co`
   - Database: `postgres`
   - User: `postgres`
   - Password: Your database password
   - Port: `5432`

## Features

- **External Database**: Connects to your existing Supabase PostgreSQL database
- **Automatic Migrations**: Runs database migrations on startup
- **Superuser Creation**: Automatically creates an admin user if it doesn't exist
- **Static Files**: Collects and serves static files
- **Production Ready**: Uses Gunicorn with multiple workers
- **Image Processing**: Includes libheif and other image processing libraries for Wagtail
- **PostgreSQL Configuration**: Pre-configured with PostgreSQL database settings

## How It Works

1. **Project Creation**: Uses `wagtail start` to create a new Wagtail project
2. **Settings Replacement**: Replaces the generated settings files with custom ones configured for PostgreSQL
3. **Database Connection**: Connects directly to your Supabase database
4. **Application Start**: Runs the application with Gunicorn

## Development

To run in development mode, you can override the settings:

```bash
docker run -e DJANGO_SETTINGS_MODULE=luoibacstudio.settings.development -e DEBUG=True ...
```

## Troubleshooting

1. **Database Connection Issues**: 
   - Verify your Supabase credentials in the `.env` file
   - Check that your Supabase database is accessible from your deployment environment
   - Ensure your IP is whitelisted in Supabase if using IP restrictions

2. **Permission Issues**: Ensure the startup script is executable (`chmod +x start.sh`)
3. **Port Conflicts**: Change the port mappings if 8000 is already in use
4. **Settings Issues**: The custom settings files are automatically copied to replace the generated ones

## Production Deployment

For production, make sure to:

1. Set a strong `SECRET_KEY`
2. Use proper Supabase database credentials
3. Configure `ALLOWED_HOSTS` to include your domain
4. Set up proper SSL/TLS
5. Set `DEBUG=False`
6. Ensure your deployment environment can reach Supabase (no firewall issues)
