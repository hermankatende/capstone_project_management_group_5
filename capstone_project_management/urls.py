from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    path('dashboard/', include('programs.dashboard_urls')),  # dashboard entry (see below)
    path('programs/', include('programs.urls')),
    path('facilities/', include('facilities.urls')),
    path('services/', include('services.urls')),
    path('equipment/', include('equipment.urls')),
    path('projects/', include('projects.urls')),
    path('participants/', include('participants.urls')),
    path('outcomes/', include('outcomes.urls')),
]
