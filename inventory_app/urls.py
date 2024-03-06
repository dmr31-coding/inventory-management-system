from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.index, name="dashboard_index"),
    path("staff/", views.staff, name="dashboard_staff"),
    path("staff/detail/<int:pk>/", views.staff_detail, name="dashboard_staff_detail"),
    path("product/", views.product, name="dashboard_product"),
    path("product/delete/<int:pk>/", views.product_delete, name="dashboard_product_delete"),
    path("product/update/<int:pk>/", views.product_update, name="dashboard_product_update"),
    path("order/", views.order, name="dashboard_order"),
    
]
