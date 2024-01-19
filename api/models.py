from django.db import models

class MainData(models.Model):
    tg_id = models.PositiveBigIntegerField(unique=True) # Telegram id
    tel_number = models.CharField(max_length=20) # Telefon raqam
    fio = models.CharField(max_length=100) # Ism, familiya, otasining ismi
    new_square = models.FloatField() # Novie kvadrat
    section = models.PositiveIntegerField() # Podiezd
    floor = models.PositiveIntegerField() # Etaj
    overall_sum = models.FloatField() # Jami summa
    paid = models.FloatField() # To'langan
    # posted_time = models.DateTimeField(auto_now_add = True) # Ushbu ma'lumot qo'yilgan vaqti
    # edited_time = models.DateTimeField(auto_now = True) # Edit qilingan vaqti

    def __int__(self):
        return self.tg_id
    
    class Meta:
        verbose_name = "Ma'lumot"
        verbose_name_plural = "Ma'lumotlar"