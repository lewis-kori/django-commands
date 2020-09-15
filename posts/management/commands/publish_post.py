from django.core.management.base import BaseCommand, CommandError
from posts.models import Category, Post

class Command(BaseCommand):
    help = 'Marks the specified blog post as published.'

    def add_arguments(self, parser):
        parser.add_argument('post_id', type=int)

    def handle(self, *args, **options):
        try:
            post = Post.objects.get(id=options['post_id'])
        except Post.DoesNotExist:
            raise CommandError(f'Post with id {options["post_id"]} does not exist')
        if post.published:
            self.stdout.write(self.style.ERROR(f'Post: {post.title} was already published'))
        else:
            post.published = True
            post.save()
            self.stdout.write(self.style.SUCCESS(f'Post: {post.title} successfully published'))
