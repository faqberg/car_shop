from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("models/",views.models,name="models"),
    path("models/<str:carname>",views.model,name="model"),
    path("edit",views.edit,name="edit"),
    path("create_car",views.create_car,name="create_car"),
    path("create_car_form",views.create_car_form,name="create_car_form"),
    path("edit_cars",views.edit_cars,name="edit_cars"),
    path("edit_car/<str:carname>",views.edit_car,name="edit_car"),
    path("edit_car_form",views.edit_car_form,name="edit_car_form"),
    path("delete_cars",views.delete_cars,name="delete_cars"),
    path("delete_car/<str:carname>",views.delete_car,name="delete_car"),
    path("delete_car_confirm",views.delete_car_confirm,name="delete_car_confirm"),
    path("delete_car_form",views.delete_car_form,name="delete_car_form"),
    path("edit_features",views.edit_features,name="edit_features"),
    path("edit_features/<str:carname>",views.edit_features_car,name="edit_features_car"),
    path("add_features/<str:carname>",views.add_features,name="add_features"),
    path("add_features_form",views.add_features_form,name="add_features_form"),
    path("edit_feature/<str:featureid>",views.edit_feature,name="edit_feature"),
    path("edit_feature_form",views.edit_feature_form,name="edit_feature_form"),
    path("delete_feature_confirm/<str:featureid>",views.delete_feature_confirm,name="delete_feature_confirm"),
    path("delete_feature_form",views.delete_feature_form,name="delete_feature_form"),
    path("edit_info",views.edit_info,name="edit_info"),
    path("edit_info/<str:carname>",views.edit_info_car,name="edit_info_car"),
    path("edit_inf/<str:infoid>",views.edit_inf,name="edit_inf"),
    path("edit_inf_form",views.edit_inf_form,name="edit_inf_form"),
    path("delete_inf_confirm/<str:infoid>",views.delete_inf_confirm,name="delete_inf_confirm"),
    path("delete_inf_form",views.delete_inf_form,name="delete_inf_form"),
    path("add_infos/<str:carname>",views.add_info,name="add_info"),
    path("add_info_form",views.add_info_form,name="add_info_form"),







    path("api/cars/", views.get_all_cars_api, name="get_all_cars_api"),
    path("api/cars/<int:pk>/", views.get_car_details_api, name="get_car_details_api"),
    path("api/cars/create/", views.create_car_api, name="create_car_api"),
    path("api/cars/<int:pk>/update/", views.update_car_api, name="update_car_api"),
    path("api/cars/<int:pk>/delete/", views.delete_car_api, name="delete_car_api"),
    path("api/car_features/", views.get_all_car_features_api, name="get_all_car_features_api"),
    path("api/car_features/<int:pk>/update/", views.update_car_feature_api, name="update_car_feature_api"),
    path("api/car_features/<int:pk>/delete/", views.delete_car_feature_api, name="delete_car_feature_api"),
    path("api/car_info/", views.get_all_car_info_api, name="get_all_car_info_api"),
    path("api/car_info/<int:pk>/update/", views.update_car_info_api, name="update_car_info_api"),
    path("api/car_info/<int:pk>/delete/", views.delete_car_info_api, name="delete_car_info_api"),
]