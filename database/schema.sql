CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE institutions (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  legal_id VARCHAR(50) NOT NULL,
  address VARCHAR(255) NOT NULL,
  logo_url TEXT,
  primary_color VARCHAR(20) DEFAULT '#1f2937',
  approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE stations (
  id BIGSERIAL PRIMARY KEY,
  institution_id BIGINT NOT NULL REFERENCES institutions(id) ON DELETE CASCADE,
  name VARCHAR(200) NOT NULL,
  location GEOGRAPHY(Point, 4326) NOT NULL,
  station_type VARCHAR(100) NOT NULL,
  responsible VARCHAR(200) NOT NULL,
  calibration_certificate_url TEXT,
  approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE sensors (
  id BIGSERIAL PRIMARY KEY,
  station_id BIGINT NOT NULL REFERENCES stations(id) ON DELETE CASCADE,
  sensor_type VARCHAR(100) NOT NULL,
  variables JSONB DEFAULT '[]',
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE measurements (
  id BIGSERIAL PRIMARY KEY,
  sensor_id BIGINT NOT NULL REFERENCES sensors(id) ON DELETE CASCADE,
  captured_at TIMESTAMP NOT NULL,
  metric VARCHAR(50) NOT NULL,
  value NUMERIC(10,2) NOT NULL,
  unit VARCHAR(20) NOT NULL
);

CREATE INDEX measurements_captured_at_metric_idx ON measurements (captured_at, metric);

CREATE TABLE alerts (
  id BIGSERIAL PRIMARY KEY,
  station_id BIGINT NOT NULL REFERENCES stations(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL,
  message TEXT NOT NULL,
  severity VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  resolved BOOLEAN DEFAULT FALSE
);
