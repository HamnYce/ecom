from base_commands.base_seed_command import BaseSeedCommand
from users.factory import UserFactory


class Command(BaseSeedCommand):
    def __init__(self, *args, **kwargs):
        self.factory = UserFactory
        super().__init__(*args, **kwargs)
