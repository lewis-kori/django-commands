import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commands.settings')

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

users = User.objects.all()

for user in users:
    print(f'user is {user.get_full_name()} and their username is {user.get_username()}')