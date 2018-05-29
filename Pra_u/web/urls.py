from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "web"


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^login/$',views.log_in,name="log_in"),
    url(r'register/$',views.sign_up,name="register"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)