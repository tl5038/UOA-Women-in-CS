try:
    import psycopg2
except ImportError:
    psycopg2 = None

import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Ensure postgres is up and running before starting the server"""

    def handle(self, *args, **options):
        if settings.DATABASES["default"]["ENGINE"] != "django.db.backends.postgresql":
            self.stdout.write("Postgres not being used, skipping wait for postgres")
            return
        if psycopg2 is None:
            self.stdout.write("psycopg2 not installed, skipping wait for postgres")
            return

        self.stdout.write("Waiting for postgres...")
        while True:
            try:
                self.check(databases=["default"])
                self.stdout.write("Postgres is up and running, continuing...")
                break
            except (OperationalError, psycopg2.OperationalError) as e:
                self.stdout.write(f"Postgres unavailable, retrying in 2 seconds... ({e})")
                time.sleep(2)
