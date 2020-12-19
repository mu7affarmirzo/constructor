from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shirtdesigner/', include('shirtdesigner.api.urls', 'menu_api')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('shirtdesigner/', include('shirtdesigner.api.urls')),
    # path('api/account/', include('account.api.urls', 'account_api')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)