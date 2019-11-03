from django.db import models

# Create your models here.

# modeles 要在admin里注册
class Gallery(models.Model):
    # CharField--字段字符 BigIntegerField--大整数字段 ImageField--图像字段
    description=models.CharField(default='在这里写作品简介',max_length=100)
    image = models.ImageField(default='default.png',upload_to='images/')
    title=models.CharField(default='作品标题',max_length=50)
    
    def __str__(self):
        return self.title

