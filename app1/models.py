from django.db import models

from django.db import models

ustatus = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]

class Registration(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=12)
    user_email = models.EmailField()
    driver_name = models.CharField(max_length=30)
    driving_license_no = models.CharField(max_length=30)
    driving_license = models.FileField(upload_to='documents/')
    vehicle_insurance = models.FileField(upload_to='documents/')
    rc_book = models.FileField(upload_to='documents/')
    address_proof = models.FileField(upload_to='documents/')
    cancelled_cheque = models.FileField(upload_to='documents/')
    fitness_certificate = models.FileField(upload_to='documents/')
    u_status = models.CharField(max_length=50, choices=ustatus, default='pending')

    def __str__(self):
        return self.user_name
