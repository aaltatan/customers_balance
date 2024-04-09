import os
from ninja import NinjaAPI
from ninja.security import django_auth
from apps.transactions.api import router as transactions_router
from apps.customers.api import router as customers_router
from django.contrib.auth.decorators import login_required

os.environ["NINJA_SKIP_REGISTRY"] = "yes"

api = NinjaAPI(
  auth=django_auth,
  description='Customer Balance Management for al Dabbagh mini market',
  title='Customer Balance Management',
  version="1.0.0",
  docs_decorator=login_required,
  urls_namespace='latest',
)

api.add_router('/transactions', transactions_router)
api.add_router('/customers', customers_router)