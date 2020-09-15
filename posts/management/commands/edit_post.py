from django.core.management.base import BaseCommand, CommandError
from posts.models import Category, Post

class Command(BaseCommand):
    help = 'Edits the specified blog post.'

    def add_arguments(self, parser):
        parser.add_argument('post_id', type=int)

        # optional arguments
        parser.add_argument('-t', '--title',type=str, help='Indicate new name of the blog post.')
        parser.add_argument('-c', '--content',type=str, help='Indicate new blog post content.')

    def handle(self, *args, **options):
        title = options['title']
        content = options['content']
        try:
            post = Post.objects.get(id=options['post_id'])
        except Post.DoesNotExist:
            raise CommandError(f'Post with id {options["post_id"]} does not exist')
        
        if title or content:
            if title:
                old_title = post.title
                post.title = title
                post.save()
                self.stdout.write(self.style.SUCCESS(f'Post: {old_title} has been update with a new title, {post.title}'))
            if content:
                post.content = content
                post.save()
                self.stdout.write(self.style.SUCCESS('Post: has been update with new text content.'))
        else:
            self.stdout.write(self.style.NOTICE('Post content remains the same as no arguments were given.'))
        
