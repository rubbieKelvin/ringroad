from .views.items import item_api
from .views.store import store_api
from .views.user import user_api

urlpatterns = [
    *item_api.paths,
    *store_api.paths,
    # Take out authentication views, we'll be using shared.apps.authentication instead
    # We'll include this if we have use for api login
    # *authentication_api.paths
    *user_api.paths,
]
