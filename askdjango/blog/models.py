#blog/modles.py
import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import ValidationError
from django.db import models



def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
    help_text="포스팅 제목을 입력해주세요. 최대 100자 내외") #길이 제한이 있는 문자열
    content = models.TextField(verbose_name="내용")    # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, 
        validators=[lnglat_validator],
        help_text='위도/경도 포멧으로 입력하세요')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   # 처음datetime이 생성될 때 자동 생성 Ture
    updated_at = models.DateTimeField(auto_now=True)    #  datetime이 저장될 때 마다.!

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
    # 저는 매번 어떠한 모델에 대해서 디테일 뷰를 만들게 되면 그즉시 get_abloute_url이라는 이 멤버 함수를 무조건 선언합니다.

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name