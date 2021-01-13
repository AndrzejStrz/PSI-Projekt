from django.db import models

class Travel(models.Model):
    Track = models.CharField(max_length=45)
    Date = models.DateField(null=False)


class Train(models.Model):
    Name = models.CharField(max_length=45)


class Ticket_Options(models.Model):
    Price = models.FloatField(null=False)
    Ticket_Name = models.CharField(max_length=45)


class Ticket(models.Model):
    Train_Ticket = models.ForeignKey(Train, on_delete=models.CASCADE, null=False)
    Ticket_Options_Ticket = models.ForeignKey(Ticket_Options, on_delete=models.CASCADE, null=False)
    Travels_Ticket = models.ForeignKey(Travel, on_delete=models.CASCADE, null=False)


class User(models.Model):
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    Login = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    Mail = models.CharField(max_length=45)
    Ticket_Ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False)


class Carriage(models.Model):
    Number_Of_Seats = models.IntegerField(null=False)
    Train_Carriage = models.ForeignKey(Train, on_delete=models.CASCADE, null=False)


class Seats(models.Model):
    Seats_Number = models.IntegerField(null=False)
    Ticket_Number = models.IntegerField(null=False)
    Carriage_Seats = models.ForeignKey(Carriage, on_delete=models.CASCADE, null=False)
