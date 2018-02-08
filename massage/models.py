from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()


class Massage(models.Model):
    KIND = (('S', 'single'),
            ('D', 'double'))

    DURATION = (('30', '30 minutes'),
                ('45', '45 minutes'),
                ('60', '60 minutes'))

    name = models.CharField(max_length=35)
    kind = models.CharField(max_length=1, choices=KIND)
    duration = models.CharField(max_length=2, choices=DURATION)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Massage: {} kind: {} duration: {}".format(self.name, self.kind, self.duration)


class Masseur(models.Model):
    GENDER = (('M', 'male'),
              ('F', 'female')
              )

    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.PositiveIntegerField()
    massages = models.ManyToManyField(Massage)

    def __str__(self):
        return self.name + ' ' + self.surname


class Rating(models.Model):
    RATES = (('1', 1),
             ('2', 2),
             ('3', 3),
             ('4', 4),
             ('5', 5))

    rate = models.CharField(max_length=1, choices=RATES)
    masseur = models.ForeignKey(Masseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.rate


class Address(models.Model):
    street_name = models.CharField(max_length=70)
    street_number = models.PositiveSmallIntegerField()
    post_code = models.CharField(max_length=6)
    city = models.CharField(max_length=35)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}, {}".format(self.street_name, self.street_number, self.city)


class Client(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    phone = models.PositiveIntegerField()
    favorites = models.ManyToManyField(Masseur, blank=True)
    addresses = models.ManyToManyField(Address)

    def __str__(self):
        return self.name + ' ' + self.surname


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)
    masseur = models.ForeignKey(Masseur, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False)
