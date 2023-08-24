from django.core.management.base import BaseCommand


class BaseSeedCommand(BaseCommand):
    help = "Seeds models"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--number',
            action='store',
            default=100,
            type=int,
            required=False,
            dest='number',
            help="use this to specify how many items to seed. default=100"
        )

    def handle(self, *args, **kwargs):
        for _ in range(kwargs['number']):
            self.factory()

        self.stdout.write(f"seeded {kwargs['number']} rows")
