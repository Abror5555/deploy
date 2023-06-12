# from portfolio.shop.views import IndexView, CategoryView
# from portfolio.shop.views import new_product, product_detail, product_update, product_delete, new_comment, delete_comment
# from django.urls import path


# urlpatterns = [

#     path('', IndexView.as_view(), name='index'),
#     path('<str:category_name>/category', CategoryView.as_view(), name='category'),

#     path("new", new_product, name='new'),
#     path("<int:product_id>/detail", product_detail, name='detail'),
#     path("<int:product_id>/update", product_update, name='update'),
#     path("<int:product_id>/delete", product_delete, name='delete'),
#     path("<int:product_id>/comment/new", new_comment, name='comment_new'),
#     path("<int:product_id>/comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),
# ]