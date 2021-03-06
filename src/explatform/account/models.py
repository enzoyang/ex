from django.db import models
#coding:UTF-8

class Sexual(models.Model):
    '''性别
    '''
    SexualValue = models.CharField(max_length=2)
    def __unicode__(self):
        return self.SexualValue

class BasicProfile(models.Model):
    '''基本资料
    '''
    RealName = models.CharField(max_length=20)#真实姓名
    Sexual = models.ForeignKey(Sexual)#性别
    Birthday = models.DateField()#生日
    Favourite = models.CharField(max_length=40)#爱好
    Homepage = models.URLField()#主页
    Location = models.CharField(max_length=100)#地址
    def __unicode__(self):
        return self.RealName

class User(models.Model):
    '''用户信息
    '''
    NickName = models.CharField(max_length=20)#昵称
    Email = models.CharField(max_length=75)#电子邮件
    Password = models.CharField(max_length=40)#密码
    
    BasicProfile = models.ForeignKey(BasicProfile)#基本资料
    def __unicode__(self):
        return self.NickName
