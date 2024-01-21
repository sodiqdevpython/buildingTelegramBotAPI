from django.db import models

class MainData(models.Model):
    tg_id = models.PositiveBigIntegerField(unique=True) # Telegram id
    tel_number = models.CharField(max_length=20) # Telefon raqam
    fio = models.CharField(max_length=100) # Ism, familiya, otasining ismi
    new_square = models.CharField(max_length=20) # Novie kvadrat
    section = models.CharField(max_length=20) # Podiezd
    floor = models.CharField(max_length=20) # Etaj
    overall_sum = models.CharField(max_length=20) # Jami summa
    paid = models.CharField(max_length=20) # To'langan
    doc_number = models.CharField(max_length=10, unique=True) # document nomeri
    doc_image = models.ImageField(upload_to='media') # document rasmi
    # posted_time = models.DateTimeField(auto_now_add = True) # Ushbu ma'lumot qo'yilgan vaqti
    # edited_time = models.DateTimeField(auto_now = True) # Edit qilingan vaqti

    def __int__(self):
        return self.tg_id

    class Meta:
        verbose_name = "Ma'lumot"
        verbose_name_plural = "Ma'lumotlar"