from django.urls import path, re_path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [

    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    # path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
    # path("archive/<year4:year>/", views.archive, name='archive'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),

]