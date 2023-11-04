from django.contrib import admin
from django.urls import path, include
from shared.tooling.postman import PostmanV2Collection

collection = PostmanV2Collection(
    url="http://localhost:8000/api",
    info=PostmanV2Collection.Info(
        name="Inventory Manager API",
        description="The Inventory Manager API is a powerful tool for efficiently managing your inventory."
        "\nIt offers a set of endpoints and functions that enable you to easily control and monitor your inventory of products or items."
        "\nWith features for creating, updating, and tracking items, as well as managing purchases, sales, and inventory adjustments,"
        "\nthis API empowers businesses to streamline their inventory management processes, reduce errors,"
        "\nand maintain accurate and up-to-date inventory records",
    ),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("postman-v2-collection/", collection.view),
    path("auth/", include("shared.apps.authentication.urls"))
]
