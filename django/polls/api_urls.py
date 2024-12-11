from django.urls import path
from . import api_views  # Assuming your API views are in `api_views.py`

urlpatterns = [
    # ex: /api/questions/
    path('questions/', api_views.QuestionViewSet.as_view({'get': 'list', 'post': 'create'}), name='question-list'),
]
