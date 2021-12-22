from django.urls import path , include

from .views import AddItemToBasket, BasketDetail, CategoryCreate, CategoryDelete, ContentCreate, OrderBasketItems



urlpatterns = [
    #url for creating a category
    #http://127.0.0.1:8000/storeapp/createcategory/
    path('createcategory/',CategoryCreate.as_view()),

    #url for deleting a category
    #http://127.0.0.1:8000/storeapp/deletecategory/
    path('deletecategory/',CategoryDelete.as_view()),

    #url for creating a content
    #http://127.0.0.1:8000/storeapp/createcontent/
    path('createcontent/',ContentCreate.as_view()),

    #url for adding an item(content) to the basket
    #http://127.0.0.1:8000/storeapp/additemtobasket/
    path('additemtobasket/',AddItemToBasket.as_view()),

    #url for getting the basket info
    #http://127.0.0.1:8000/storeapp/basketdetail/
    path('basketdetail/',BasketDetail.as_view()),

    #url for ordering the basket items
    #http://127.0.0.1:8000/storeapp/orderbasketitems/
    path('orderbasketitems/',OrderBasketItems.as_view()),
]