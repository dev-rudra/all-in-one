# POSTGRESQL

# Install `postgresql` from the [official site](https://www.postgresql.org/download/).

> [!TIP]
> Create `.zprofile` or `.zshrc` file on your home and export the psql binary path `export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"`
> And restart your terminal

# Connect to postgres DB
```sql
psql -U postgres
```

### Create a new DB
```sql
CREATE DATABASE db_name
```

### Create a new user with read/write permission
```sql
CREATE USER user_name WITH PASSWORD 'securepassword';

--- grant privileges on the new database
GRANT CONNECT ON DATABASE db_name TO user_name;
```


### Grant usage on schema and read/write on all tables
Switch to database

```sql
\c db_name
```

Then:
```sql
--- give access to the public schema (default schema)
GRANT USAGE ON SCHEMA public TO user_name;

--- grant privileges to create and use tables
GRANT CREATE ON SCHEMA public TO user_name;

--- [Optional] : allow read/write on all existing tables
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO user_name;

--- Ensure future tables are accessable 
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO user_name;
```

