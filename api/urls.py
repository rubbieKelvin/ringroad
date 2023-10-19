from .views.items import item_api
from .views.store import store_api
from .views.user import authentication_api

urlpatterns = [
    *item_api.paths,
    *store_api.paths,
    *authentication_api.paths
]