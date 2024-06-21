from django.db import models
from django.urls import reverse

from datetime import date as dt


# Create your models here.
class Company( models.Model ):
    name = models.CharField( verbose_name='Company Name', max_length=255 )
    registrationNumber = models.CharField( null=False, max_length=255 )
    address = models.TextField()
    companyId = models.BigAutoField( primary_key=True )
    contactPersonName = models.CharField( null=True, max_length=255 )
    contactPersonNumber = models.CharField( null=True, max_length=255, blank=True )
    contactPersonEmail = models.CharField( null=True, max_length=255, blank=True )

    def __str__( self ) -> str:
        return f'{self.name} ({self.registrationNumber})'

    def get_absolute_url( self ):
        return reverse( "company_detail", kwargs={ "pk": self.pk} )


class Department( models.Model ):
    departmentId = models.BigAutoField( primary_key=True )
    departmentName = models.CharField( null=False, max_length=255 )
    company = models.ForeignKey( Company, on_delete=models.CASCADE, related_name='departments' )

    def __str__( self ):
        return self.departmentName

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"id": self.pk})
    


class Employee( models.Model ):
    firstName = models.CharField( null=False, max_length=255 )
    lastName = models.CharField( null=False, max_length=255 )
    emailAddress = models.EmailField( null=True )
    phoneNumber = models.CharField( null=True, max_length=255 )
    dateStarted = models.DateField( default=dt.today )
    dateLeft = models.DateField( null=True, blank=True )
    duties = models.TextField( blank=True, null=True )
    company = models.ForeignKey( Company, on_delete=models.CASCADE, related_name='employees' )
    department = models.ForeignKey( Department, models.CASCADE, related_name='employees' )
    personId = models.BigAutoField( primary_key=True )

    def __str__( self ) -> str:
        return self.firstName + ' ' + self.lastName
