package main

type Fighter struct {
	ID   int    `db:"id"`
	Name string `db:"name"`
}

type Stats struct {
	ID        int `db:"id"`
	FighterID int `db:"fighter_id"`
	Strikes   int `db:"strikes"`
}

type Fight struct {
	ID         int `db:"id"`
	FighterIDB int `db:"fighter_id_b"`
	FighterIDA int `db:"fighter_id_a"`
	StatsID    int `db:"stats_id"`
	Result     int `db:"result"`
}
