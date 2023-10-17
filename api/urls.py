from .views.user import authentication_api

urlpatterns = [
    *authentication_api.paths
]