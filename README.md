# VRISA - Entrega práctica

Implementación base para la plataforma **VRISA** usando el stack solicitado (Django + PostGIS, React y Expo).

## Backend (Django + PostGIS)

- API REST con autenticación JWT.
- Modelos para instituciones, estaciones, sensores, mediciones y alertas.
- Filtros básicos para búsqueda y ordenamiento.

### Ejecutar

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

### Endpoints principales

- `POST /api/auth/token/` -> login JWT
- `GET /api/institutions/`
- `GET /api/stations/`
- `GET /api/measurements/`
- `GET /api/alerts/`

## Frontend (React)

Dashboard básico que consulta estaciones desde la API.

```bash
cd frontend
npm install
npm run dev
```

## Mobile (Expo)

Pantalla móvil inicial para listar alertas.

```bash
cd mobile
npm install
npx expo start
```

## Docker Compose (opcional)

```bash
docker compose up --build
```

## Base de datos (scripts)

Los scripts SQL y el diccionario de datos se encuentran en `database/`:

- `database/schema.sql`
- `database/seed.sql`
- `database/data_dictionary.md`
