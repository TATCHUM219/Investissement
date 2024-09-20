from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings
app_name='client'
urlpatterns = [
    path('',views.index),
    path('test/',views.test),
    path('register/',views.register,name='register'),
    path('validatenom/',csrf_exempt(views.validateurNom.as_view()),name='validatenom'),
    path('validateemail/',csrf_exempt(views.validateurEmail.as_view()),name='validateemail'),
    path('validatetelephone/',csrf_exempt(views.validateurTelephone.as_view()),name='validatetelephone'),
    path('login/',views.login,name='login'),
    path('produits/',views.produits,name='produits'),
    path('compte/<int:id_clt>',views.compte,name='compte'),
    path('logout/',views.logout,name='logout'),
    path('achat/<int:id_clt>/<int:id_mach>',views.achat,name='achat'),
    path('minage/<int:id_ach>',views.minage,name='minage'),
    path('prochain_minage/<int:id_ach>',views.prochainMin),
    path('depot/',views.depot),
    path('retrait/',views.retrait),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)