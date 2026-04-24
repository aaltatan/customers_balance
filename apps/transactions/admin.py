from django.contrib import admin
from django.utils.html import format_html

from apps.core.utils import dict_to_css

from .models import Transaction

STYLES: dict[str, str] = {
    "color": "white",
    "font-weight": "bold",
    "padding": ".25em .5em",
    "border-radius": ".5em",
    "display": "block",
}


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("customer__name",)
    list_display = ("customer", "debit_cur", "credit_cur", "date", "user")
    list_per_page = 10
    ordering = ("-date",)
    sortable_by = ("customer", "date")
    list_filter = ("user__username",)
    autocomplete_fields = ("customer",)
    fields = (
        ("date"),
        ("debit", "credit"),
        "customer",
        "user",
    )

    @admin.display(description="debit_cur")
    def debit_cur(self, obj: Transaction):
        styles = dict_to_css({"background-color": "orangered", **STYLES})
        return format_html(f"<span style={styles if obj.debit else ''}>{obj.debit:,}</span>")

    @admin.display(description="credit_cur")
    def credit_cur(self, obj: Transaction):
        styles = dict_to_css({"background-color": "green", **STYLES})
        return format_html(f"<span style={styles}>{obj.credit:,}</span>")
