from django.db import models

class Customer(models.Model):
    customerId = models.IntegerField()
    name = models.CharField(max_length = 50, blank = False)
    address = models.CharField(max_length = 200, blank = True)
    credit = models.IntegerField()
    status = models.BooleanField()
    joinedDate = models.DateTimeField()

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format( \
            self.customerId, self.name,self.address, \
            self.credit, self.status, self.joinedDate)
