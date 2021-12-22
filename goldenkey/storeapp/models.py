from django.db import models

from users.models import CustomUser

# Create your models here.


#Category Model
class Category(models.Model):
    title = models.CharField(max_length=100)




#Content Model
class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank=True)
    # cost = 0 ==> free , otherwise ==> paid
    cost = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)




#Basket Model
class Basket(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    
    #Calculate total price
    @property
    def totalPrice(self):
        basketItems = BasketItem.objects.filter(basket = self)
        result = 0
        for item in basketItems:
            result += item.price
        return result



#Basket Items Model
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.quantity * self.content.cost



#Order Model
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
