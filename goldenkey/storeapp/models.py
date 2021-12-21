from django.db import models

from goldenkey.users.models import CustomUser

# Create your models here.


class Category(models.Model):
    title = models.CharField()



class Content(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank=True)
    # cost = 0 ==> free , otherwise ==> paid
    cost = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)



class Basket(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    totalPrice = models.FloatField(default=0)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.quantity * self.content.cost