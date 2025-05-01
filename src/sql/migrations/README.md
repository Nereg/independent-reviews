Example usage to migrate up:
1) Modify the migrate.yaml file:
    - include the DB connection URL (for example from the YAML config). Make sure it is URL encoded!
    - modify the Go Migrate command, if needed (https://github.com/golang-migrate/migrate/tree/master/cmd/migrate)
    - rename it to migrate.yaml.secret
2) Run `docker compose -f docker-compose.yaml -f docker-compose.migrate.yaml.secret up -d` to execute the Go Migrate command
    - `create` creates files for a new migration
    - `up` brings up a schema with all the migrations