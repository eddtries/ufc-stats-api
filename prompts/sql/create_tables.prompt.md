Convert the following DBML to valid PostgreSQL, following all rules.

Rules: 
1. All tables must be CREATE TABLE IF NOT EXISTS.
2. All primary keys must be auto-incrementing.
3. Only include valid postgresql code in your answer, do not describe anything in text.

```
Table fighter {
  id integer [primary key]
  name string
}

Table fight {
  id integer [primary key]
  fighter_id_b integer [ref: - fighter.id]
  fighter_id_a integer [ref: - fighter.id]
  stats_id integer [ref: < stats.id]
  result integer
}

Table stats {
  id integer [primary key]
  fighter_id  integer [ref: - fighter.id]
  strikes integer
}
```
