from os import environ


def get_db_name():
    return 'primary' if environ['ENVIRONMENT'] == 'Production' else 'default'


class DatabaseRouter:
    """Database router that uses the 'primary' database on production environment and 'default' on all others"""

    def db_for_read(self, model, **hints):
        return get_db_name()

    def db_for_write(self, model, **hints):
        return get_db_name()
    