from django.contrib import admin
from .models import Transaction
from django.utils.html import format_html

styles: dict[str, str] = {
    'color': 'white',
    'font-weight': 'bold',
    'padding': '.25em .5em',
    'border-radius': '.5em',
    'display': 'block',
}

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    search_fields = ['customer__name']
    list_display = [
        "customer",
        "debit_cur",
        "credit_cur",
        "date",
        "user",
    ]
    list_per_page = 10
    ordering = ["-date"]
    sortable_by = ["customer", "date"]
    list_filter = ['user__username']

    @admin.display(description="debit_cur")
    def debit_cur(self, obj: Transaction):
        s: dict[str, str] = {
            'background-color': 'orangered',
            **styles
        }
        inline: str = \
              'style="' + ';'.join([f'{k}:{v}' for k, v in s.items()]) + '"'
        return format_html(
            f"<span {inline if obj.debit else ''}>{obj.debit:,}</span>"
        )

    @admin.display(description="credit_cur")
    def credit_cur(self, obj: Transaction):
        s: dict[str, str] = {
            'background-color': 'green',
            **styles
        }
        inline: str = \
              'style="' + ';'.join([f'{k}:{v}' for k, v in s.items()]) + '"'
        return format_html(
            f"<span {inline if obj.credit else ''}>{obj.credit:,}</span>"
        )
