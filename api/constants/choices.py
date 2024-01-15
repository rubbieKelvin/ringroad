from django.db.models import TextChoices


class PropertyTypes(TextChoices):
    TEXT = "TEXT"
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    DATE = "DATE"
    DATETIME = "DATETIME"
    TIME = "TIME"
