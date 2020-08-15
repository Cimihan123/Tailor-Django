
from django.urls import path , include
from  . import views




urlpatterns = [
    path('', views.index, name='index'),
      path('info/', views.info, name='info'),
        path('features/', views.features, name='features'),
          path('product_detail/', views.productDetail, name='product_detail'),
            path('cart/', views.listCart, name='cart'),

              path('add/', views.add, name='add'),
                path('add/' ,views.success, name='success'),
                  path('updating/<int:pk>/', views.whatUpdate, name='updating'),
                    path('contact-female/<str:pk>/', views.contactUpdate, name='contact-female'),
                     path('contact-male/<str:pk>/', views.contactUpdate1, name='contact-male'),
                     # path('update-male/<str:pk>/', views.maleUpdate, name='update-male'),
                    #   path('update-female/<str:pk>/', views.femaleUpdate, name='update-female'),
                        path('delete/<str:pk_test>/' ,views.delete, name='delete'),
    

]
