from django.urls import (
    #include,
    path,
    re_path,
    #register_converter,
)
from django.views.generic import (
    TemplateView,
    #RedirectView,
)

from .views import ConstructionBidClassCreateView


urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    path('', ConstructionBidClassCreateView.as_view(), name='index'),  
]



# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
