from base_commands.base_seed_command import BaseSeedCommand
from profiles.factory import UserProfileFactory


class Command(BaseSeedCommand):
    def __init__(self, *args, **kwargs):
        self.factory = UserProfileFactory
        super().__init__(*args, **kwargs)
