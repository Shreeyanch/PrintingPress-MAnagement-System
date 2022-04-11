from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("administration",views.login,name="login"),
    path("Login",views.Login,name="Login"),
    path("press", views.press, name="press"),
    path("inventory", views.inventory, name="inventory"),
    path("add",views.add, name="add"),
    path("add1",views.add1, name="add1"),
    path("add2",views.add2, name="add2"),
    path("add3",views.add3, name="add3"),

    path("edit",views.Edit, name="edit"),
    path("edit1",views.Edit1, name="edit"),
    path("edit2",views.Edit2, name="edit2"),
    path("edit3",views.Edit3, name="edit3"),

    path("delete/<str:id>",views.Delete,name="delete"),
    path("delete1/<str:id>",views.Delete1,name="delete1"),
    path("delete2/<str:id>",views.Delete2,name="delete2"), 
    path("delete3/<str:id>",views.Delete3,name="delete3"), 

    path("update/<str:id>",views.Update, name="update"),
    path("update1/<str:id>",views.Update1, name="update1"),
    path("update2/<str:id>",views.Update2, name="update2"),
    path("update3/<str:id>",views.Update3, name="update3"),

    
]