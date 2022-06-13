from django.conf import settings
from django.urls import path
from app import views
from  django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls.static import static
urlpatterns = [
    path('',views.ProductView.as_view(), name = "home"),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    
    path('cart/',views.show_cart,name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'app/login.html',authentication_form = LoginForm), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('checkout/', views.checkout, name='checkout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration")
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


