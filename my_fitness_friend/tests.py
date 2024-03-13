from django.test import TestCase
from .database_router import DatabaseRouter
from os import environ


class DatabaseRouterTests(TestCase):
    def test_db_for_read_returns_primary_given_production_environment(self):
        environ['ENVIRONMENT'] = 'Production'
        router = DatabaseRouter()
        result = router.db_for_read(None)
        self.assertEqual('primary', result)

    def test_db_for_read_returns_default_given_non_production_environment(self):
        environ['ENVIRONMENT'] = 'Development'
        router = DatabaseRouter()
        result = router.db_for_read(None)
        self.assertEqual('default', result)

    def test_db_for_write_returns_primary_given_production_environment(self):
        environ['ENVIRONMENT'] = 'Production'
        router = DatabaseRouter()
        result = router.db_for_write(None)
        self.assertEqual('primary', result)

    def test_db_for_write_returns_default_given_non_production_environment(self):
        environ['ENVIRONMENT'] = 'Development'
        router = DatabaseRouter()
        result = router.db_for_write(None)
        self.assertEqual('default', result)
