CREATE TABLE IF NOT EXISTS fighter (
  fighter_id INT NOT NULL,
  name varchar(100) NOT NULL,
  PRIMARY KEY (fighter_id)
);

CREATE TABLE IF NOT EXISTS fight (
  fight_id INT NOT NULL,
  PRIMARY KEY (fight_id)
);
