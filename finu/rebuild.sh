
#! bin/bash
docker-compose build
docker-compose up -d db
docker-compose run --rm api /bin/bash -c "cd /opt/services/api/src && python -c  \'import database; database.init_db()\'"
docker-compose up

