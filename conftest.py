import pytest


@pytest.fixture
def dashboard_db(settings):
    settings.DATABASES["dashboard"]["OPTIONS"] = {
        "options": "-c default_transaction_read_only=on -c statement_timeout=100"
    }