from django.db import models

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
rating_choice=(
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"),
)

class Article(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    rating=models.CharField(max_length=2,
        choices=rating_choice,
        default="5"
    )
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title