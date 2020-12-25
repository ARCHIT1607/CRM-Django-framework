from accounts.models import *
# Returns all customers from customer table
customers = Customer.objects.all()

# Returs first customer in table
firstCustomer = Customer.objects.first()

# Returs last customer in table
lastCustomer = Customer.objects.last()

# Returs single customer by name
customerByName = Customer.objects.get(name='Sam')

# Returs single customer by id
customerById = Customer.objects.get(id=2)

# Returs single customer in table
customerByName = Customer.objects.get(name='Sam')

# Returs all orders related to cusotmer(firstCustomer variable set above)
firstCustomer.order_set.all()

# Returs orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# Orders/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# Returs all products with tag of sports: (Query Many to Many Fields)
productFiltered = Product.objects.filter(tags__name="sports")

# returns the total count for number of times a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.produc.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Related SET example


class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)


parent = ParentModel.objects.first()
# returns all child models related to parent
parent.childmodel_set.all()
