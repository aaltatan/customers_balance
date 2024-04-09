from django.contrib import admin
from .models import Customer
from django.db.models import Count, Sum, F
from django.utils.html import format_html


styles: dict[str, str] = {
    'color': 'white',
    'font-weight': 'bold',
    'padding': '.25em .5em',
    'border-radius': '.5em',
    'display': 'block',
    'background-color': 'red',
}
styles_inline: str = ";".join([f'{k}:{v}' for k, v in styles.items()])


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
        "transactions_count",
        "net",
    ]
    sortable_by = ["name", "transactions_count", "net", "added_at"]

    class Meta:
        ordering = ["name"]

    def get_queryset(self, request):
        # Annotate the queryset with the transaction count
        queryset = (
            super()
            .get_queryset(request)
            .annotate(
                transactions_count=Count("transaction"),
                net=Sum(F('transaction__debit') - F('transaction__credit')),
            )
        )
        return queryset

    def transactions_count(self, obj):
        c = f'{obj.transactions_count:,}' if obj.transactions_count else 0
        if c == 0:
            c = format_html(
                f'<span style="{styles_inline}">{c}</span>',
            )
        return c

    def net(self, obj):
        n = f'{obj.net:,}' if obj.net else 0
        if n == 0:
            n = format_html(
                f'<span style="{styles_inline}">{n}</span>',
            )
        return n
    
    transactions_count.admin_order_field = "transactions_count"  # Specify sorting attribute
    net.admin_order_field = "net"  # Specify sorting attribute
    
