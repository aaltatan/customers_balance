from typing import Any

from django.contrib import admin
from django.utils.html import format_html

from apps.core.utils import dict_to_css

from .models import Customer

STYLES: dict[str, str] = {
    "color": "white",
    "font-weight": "bold",
    "padding": ".25em .5em",
    "border-radius": ".5em",
    "display": "block",
    "background-color": "red",
}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "added_at", "transactions_count", "net")
    sortable_by = ("name", "transactions_count", "net", "added_at")
    search_fields = ("name",)

    class Meta:
        ordering = ("name",)

    def transactions_count(self, obj: Any):
        return format_html(
            f'<span style="{dict_to_css(STYLES)}">{obj.transactions_count:,}</span>',
        )

    def net(self, obj: Any):
        return format_html(
            f'<span style="{dict_to_css(STYLES)}">{obj.net:,}</span>',
        )

    transactions_count.admin_order_field = "transactions_count"  # Specify sorting attribute
    net.admin_order_field = "net"  # Specify sorting attribute
