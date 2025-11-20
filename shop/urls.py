from django.urls import path
from .views import *
urlpatterns = [
    path("", shop_map, name="shop_map"),
    path("create/", create_shop, name="create_shop"),
    path("update/<int:pk>/", update_shop, name="update_shop"),
    path("delete/<int:pk>/", delete_shop, name="delete_shop"),
    path("view_shops", view_shops, name="view_shops"),
    path("login/", custom_login, name="login"),
    path("signup/", signup_view, name="signup"),

]


