from django.db import models

class Travel(models.Model):
    Track = models.CharField(max_length=45)
    Date = models.DateTimeField(null=False)

    def __str__(self):
       return self.Track+ ' '+ str(self.Date)

class Train(models.Model):
    Name = models.CharField(max_length=45)

    def __str__(self):
        return self.Name

class Ticket_Options(models.Model):
    Price = models.FloatField(null=False)
    Ticket_Name = models.CharField(max_length=45)

    def __str__(self):
        return self.Ticket_Name + ' ' +str(self.Price)+ ' zł '


class User(models.Model):
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    Login = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    Mail = models.CharField(max_length=45)

    def __str__(self):
        return self.Name+ ' ' + self.Surname

class Ticket(models.Model):
    Train_Ticket = models.ForeignKey(Train, on_delete=models.CASCADE, null=False,related_name='Train_Tickets')
    Ticket_Options_Ticket = models.ForeignKey(Ticket_Options, on_delete=models.CASCADE, null=False,
                                              related_name='Ticket_Options_Ticket')
    Travels_Ticket = models.ForeignKey(Travel, on_delete=models.CASCADE, null=False,related_name='Travel_Tickets')
    Ticket_User = models.ForeignKey(User, on_delete=models.CASCADE,null=False,related_name='Tickets')

    def __str__(self):
        return self.Train_Ticket+ ' '+self.Ticket_Options_Ticket+ ' '+self.Travels_Ticket+ ' '+self.Ticket_User

class Carriage(models.Model):
    Number_Of_Seats = models.IntegerField(null=False)
    Train_Carriage = models.ForeignKey(Train, on_delete=models.CASCADE, null=False, related_name='Carriages')

    def __str__(self):
        return str(self.Number_Of_Seats)

class Seats(models.Model):
    Seats_Number = models.IntegerField(null=False)
    Ticket_Number = models.IntegerField(null=False)
    Carriage_Seats = models.ForeignKey(Carriage, on_delete=models.CASCADE, null=False, related_name='Seats')

    def __str__(self):
        return str(self.Carriage_Seats)