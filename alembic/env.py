import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context
from app.models import Tariff

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models metadata
from app.database import Base

target_metadata = Base.metadata


def get_database_url():
    return os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:12345678@postgres:5432/tariffs_db",
    )


def run_migrations_offline():
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(get_database_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
