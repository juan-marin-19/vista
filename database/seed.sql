INSERT INTO institutions (name, legal_id, address, logo_url, approved)
VALUES ('DAGMA', '900123456', 'Cali, Colombia', 'https://example.com/logo.png', true);

INSERT INTO stations (institution_id, name, location, station_type, responsible, approved)
VALUES (1, 'Estación Centro', ST_GeogFromText('POINT(-76.531985 3.451648)'), 'Urbana', 'Equipo DAGMA', true);

INSERT INTO sensors (station_id, sensor_type, variables, is_active)
VALUES (1, 'Calidad del aire', '["PM2.5", "PM10", "NO2", "O3"]', true);

INSERT INTO measurements (sensor_id, captured_at, metric, value, unit)
VALUES
  (1, NOW() - INTERVAL '5 hours', 'PM2.5', 23.0, 'µg/m³'),
  (1, NOW() - INTERVAL '4 hours', 'PM2.5', 22.1, 'µg/m³'),
  (1, NOW() - INTERVAL '3 hours', 'PM2.5', 21.4, 'µg/m³');

INSERT INTO alerts (station_id, title, message, severity)
VALUES (1, 'Alerta preventiva', 'Nivel de PM2.5 en aumento.', 'media');
