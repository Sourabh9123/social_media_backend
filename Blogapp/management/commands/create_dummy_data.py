from django.core.management.base import BaseCommand
from Blogapp.models import blog
from account.models import User
from django.contrib.auth import get_user_model
from faker import Faker



User = get_user_model()
fake = Faker()


# Assuming you have an existing user or create one if not



class Command(BaseCommand):
    help = 'Creates dummy data'

    
    
    def handle(self, *args, **kwargs):
        
        user_id = 'f2ae599c-b113-47e5-a435-012737fbad8b'
        try:
            user = User.objects.get(id=user_id)
            print(user)
        except User.DoesNotExist:
            pass

        # Create a Blog instance with dummy data
        blogs = blog.objects.create(
            user=user,
            title=fake.sentence(),
            content=fake.paragraph(),
            
        )
        
        print(blogs)

# Print the created blog for confirmation
# print(f"Created Blog: {blogs}")











# User_Id =  '30ae04dc-156f-45dd-9fc1-33a9fb00703d'

# user = User.objects.get(uuid=User_Id)
# print(user)

# # Create a Product instance
# # blogs = blog.objects.create(
# #    user = 

# # )