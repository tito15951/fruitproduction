from . import stripe
from ..models import Usuario as user


def create_customer(user):
    customer = stripe.Customer.create(
        description=user.nombre #Una simple descripción del usuario
    )
    return customer
user = user.objects.get(pk=1)

customer = create_customer(user)

user.customer_id = customer.id
user.save()