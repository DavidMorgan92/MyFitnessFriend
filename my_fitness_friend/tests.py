from django.test import TestCase
from unittest.mock import patch
from .database_router import DatabaseRouter


class DatabaseRouterTests(TestCase):
    @patch.dict('os.environ', {'ENVIRONMENT': 'Production'})
    def test_db_for_read_returns_primary_given_production_environment(self):
        router = DatabaseRouter()
        result = router.db_for_read(None)
        self.assertEqual('primary', result)

    @patch.dict('os.environ', {'ENVIRONMENT': 'Development'})
    def test_db_for_read_returns_default_given_non_production_environment(self):
        router = DatabaseRouter()
        result = router.db_for_read(None)
        self.assertEqual('default', result)

    @patch.dict('os.environ', {'ENVIRONMENT': 'Production'})
    def test_db_for_write_returns_primary_given_production_environment(self):
        router = DatabaseRouter()
        result = router.db_for_write(None)
        self.assertEqual('primary', result)

    @patch.dict('os.environ', {'ENVIRONMENT': 'Development'})
    def test_db_for_write_returns_default_given_non_production_environment(self):
        router = DatabaseRouter()
        result = router.db_for_write(None)
        self.assertEqual('default', result)
