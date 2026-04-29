-- VIEW 1: Leituras por Hora 
CREATE OR REPLACE VIEW view_temporal AS
SELECT 
    DATE_TRUNC('hour', TO_TIMESTAMP(timestamp, 'DD-MM-YYYY HH24:MI')) AS hora,
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- VIEW 2: Média, Max e Min por Dispositivo 
CREATE OR REPLACE VIEW view_estatisticas AS
SELECT 
    device_id AS dispositivo,
    AVG(temperature) AS media_temp,
    MAX(temperature) AS max_temp,
    MIN(temperature) AS min_temp
FROM temperature_readings
GROUP BY device_id;

-- VIEW 3: Anomalias 
CREATE OR REPLACE VIEW view_anomalias AS
SELECT *
FROM temperature_readings
WHERE temperature > 35 OR temperature < 15;

