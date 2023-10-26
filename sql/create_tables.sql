-- Create fighter table if it doesn't exist
CREATE TABLE IF NOT EXISTS fighter (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

-- Create fight table if it doesn't exist
CREATE TABLE IF NOT EXISTS fight (
    id SERIAL PRIMARY KEY,
    fighter_id_b INTEGER,
    fighter_id_a INTEGER,
    FOREIGN KEY (fighter_id_b) REFERENCES fighter(id),
    FOREIGN KEY (fighter_id_a) REFERENCES fighter(id)
);