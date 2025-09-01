from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    path('dashboard/', include('apps.programs.dashboard_urls')),  # dashboard entry (see below)
    path('programs/', include('apps.programs.urls')),
    path('facilities/', include('apps.facilities.urls')),
    path('services/', include('apps.services.urls')),
    path('equipment/', include('apps.equipment.urls')),
    path('projects/', include('apps.projects.urls')),
    path('participants/', include('apps.participants.urls')),
    path('outcomes/', include('apps.outcomes.urls')),
]
