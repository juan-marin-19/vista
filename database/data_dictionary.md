# Diccionario de datos VRISA

## Institutions
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | BIGSERIAL | Identificador único de la institución. |
| name | VARCHAR(200) | Nombre oficial de la institución. |
| legal_id | VARCHAR(50) | NIT o identificación legal. |
| address | VARCHAR(255) | Dirección física de la institución. |
| logo_url | TEXT | URL del logo institucional. |
| primary_color | VARCHAR(20) | Color principal para branding. |
| approved | BOOLEAN | Estado de aprobación de la institución. |

## Stations
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | BIGSERIAL | Identificador único de la estación. |
| institution_id | BIGINT | FK a institutions. |
| name | VARCHAR(200) | Nombre de la estación. |
| location | GEOGRAPHY(Point, 4326) | Coordenadas geográficas. |
| station_type | VARCHAR(100) | Tipo de estación (urbana, industrial, etc.). |
| responsible | VARCHAR(200) | Responsable técnico. |
| calibration_certificate_url | TEXT | Enlace a certificado de calibración. |
| approved | BOOLEAN | Estado de aprobación de la estación. |

## Sensors
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | BIGSERIAL | Identificador único del sensor. |
| station_id | BIGINT | FK a stations. |
| sensor_type | VARCHAR(100) | Tipo de sensor. |
| variables | JSONB | Variables que mide. |
| is_active | BOOLEAN | Estado activo. |

## Measurements
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | BIGSERIAL | Identificador único de medición. |
| sensor_id | BIGINT | FK a sensors. |
| captured_at | TIMESTAMP | Fecha y hora de captura. |
| metric | VARCHAR(50) | Métrica medida (PM2.5, NO2, etc.). |
| value | NUMERIC(10,2) | Valor numérico. |
| unit | VARCHAR(20) | Unidad de medida. |

## Alerts
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | BIGSERIAL | Identificador único de alerta. |
| station_id | BIGINT | FK a stations. |
| title | VARCHAR(200) | Título de alerta. |
| message | TEXT | Mensaje detallado. |
| severity | VARCHAR(20) | Severidad (baja, media, alta). |
| created_at | TIMESTAMP | Fecha de creación. |
| resolved | BOOLEAN | Estado de resolución. |
