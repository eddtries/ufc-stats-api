Generate valid Golang types for the following PostgreSQL code, following all rules.

Rules:
1. Only include valid golang code in your answer, do not write any additional text.

```
-- Create fighter table if it doesn't exist
CREATE TABLE IF NOT EXISTS fighter (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

-- Create stats table if it doesn't exist
CREATE TABLE IF NOT EXISTS stats (
    id SERIAL PRIMARY KEY,
    fighter_id INTEGER REFERENCES fighter(id),
    strikes INTEGER
);

-- Create fight table if it doesn't exist
CREATE TABLE IF NOT EXISTS fight (
    id SERIAL PRIMARY KEY,
    fighter_id_b INTEGER REFERENCES fighter(id),
    fighter_id_a INTEGER REFERENCES fighter(id),
    stats_id INTEGER REFERENCES stats(id),
    result INTEGER,
    PRIMARY KEY (fighter_id_b, fighter_id_a),
    FOREIGN KEY (stats_id) REFERENCES stats(id)
);

```