import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commands.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
from posts.models import Category, Post

User = get_user_model()

def select_category():
    categories = Category.objects.all().order_by('created_at')
    print('Please select a category for your post: ')
    for category in categories:
        print(f'{category.id}: {category}')
    category_id = input()
    category = Category.objects.get(id=category_id)
    return category


def select_author():
    users = User.objects.all()
    print('Please select an author for your post: ')
    for user in users:
        print(f'{user.id}: {user}')
    user_id = input()
    user = User.objects.get(id=user_id)
    return user
    
    

def create_post():
    title = input("Title of your post: ")
    content = input("Long post content: ")
    category = select_category()
    author = select_author()
    Post(**locals()).save()
    print('Post created successfully!')

if __name__ == "__main__":
    create_post()
