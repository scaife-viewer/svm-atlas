import os

from django.core.management import call_command
from django.core.management.base import BaseCommand

from sv_mini_atlas.library import importers, tokenizers


class Command(BaseCommand):
    """
    Prepares the database
    """

    help = "Prepares the database"

    def handle(self, *args, **options):
        if os.path.exists("db.sqlite3"):
            os.remove("db.sqlite3")
            self.stdout.write("--[Removed existing database]--")

        self.stdout.write("--[Creating database]--")
        call_command("migrate")

        self.stdout.write("--[Loading versions]--")
        importers.import_versions()

        self.stdout.write("--[Tokenizing the Iliad]--")
        tokenizers.tokenize_text_parts("urn:cts:greekLit:tlg0012.tlg001.perseus-grc2:")
