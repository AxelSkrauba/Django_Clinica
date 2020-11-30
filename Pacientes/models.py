from django.db import models

# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    email = models.EmailField()
    medical_history = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Doctors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patients = models.ManyToManyField(Patients)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Consultations(models.Model):
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        id_pretty = "Consulta para {} el {} a las {} con {}".format(self.patient, self.date, self.time, self.doctor)
        return id_pretty

