#!/usr/bin/env bash

USAGE=$(cat << EOM
This script will drop and recreate the vamble-db tables.
Ensure to run this script within a python virtual environment that has vamble-db as a dependency.

Usage:
./recreate_db.sh DB_STRING

where DB_STRING is the connection string to the database.
EOM
)

DB_STRING=$1

if [[ -z "$DB_STRING" ]]; then
    echo "$USAGE"
    exit 1
fi

RECREATE_TABLES=$(cat << EOM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import vamble_db
db_uri = '$DB_STRING'
db_engine = create_engine(db_uri, echo=True)
vamble_db.base.Base.metadata.drop_all(db_engine)
vamble_db.base.Base.metadata.create_all(db_engine)
EOM
)

echo "$RECREATE_TABLES" | python
