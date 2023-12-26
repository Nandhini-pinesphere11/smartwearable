from django.db import models
from django.utils.crypto import get_random_string

class PickupRequest(models.Model):
    STATUS_CHOICES = (
        ('accept', 'Accepted'),
        ('decline', 'Declined'),
        ('open', 'Open'),
    )

    ticket_id = models.CharField(max_length=20, unique=True)
    new_ticket_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    product_name = models.CharField(max_length=255)
    variant_no = models.CharField(max_length=50)
    problem_category = models.CharField(max_length=100)
    problem_description = models.TextField()
    date_of_purchase = models.DateField()
    invoice_copy = models.FileField(upload_to='invoice_copies/')
    issue_voice = models.FileField(upload_to='issue_voices/')
    front_image = models.FileField(upload_to='front_images/')
    back_image = models.FileField(upload_to='back_images/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def save(self, *args, **kwargs):
        # Generate a new_ticket_id if it doesn't exist
        if not self.new_ticket_id:
            self.new_ticket_id = self.generate_new_ticket_id()

        super().save(*args, **kwargs)

    def generate_new_ticket_id(self):
        # Generate a new ticket ID using a formatted string
        return f'TKT-NW-{self.get_next_ticket_number():03d}'

    def get_next_ticket_number(self):
        # Get the next available ticket number
        last_ticket = PickupRequest.objects.filter(new_ticket_id__startswith='TKT-NW-').order_by('-new_ticket_id').first()
        if last_ticket:
            last_number = int(last_ticket.new_ticket_id.split('-')[-1])
            return last_number + 1
        else:
            return 1
    
    def __str__(self):
        return f"PickupRequest - Ticket ID: {self.ticket_id}, New Ticket ID: {self.new_ticket_id}"


class CustomerDetails(models.Model):
    ticket_id = models.OneToOneField(PickupRequest, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_mobile_no = models.CharField(max_length=15)
    customer_email_id = models.EmailField()

    def __str__(self):
        return f"CustomerDetails - Ticket ID: {self.ticket_id}, Customer Name: {self.customer_name}"

class CustomerAddress(models.Model):
    customer_details = models.OneToOneField(CustomerDetails, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"CustomerAddress - Ticket ID: {self.customer_details.ticket_id}, Customer Name: {self.customer_details.customer_name}"
