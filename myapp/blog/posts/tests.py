from django.test import TestCase, Client #Client es para realizar GET requests en las vistas
from django.urls import reverse, resolve #Para las URL
from posts.models import Post #Para crear objetos 'post'
from posts.views import index, post #Para las URL y las vistas
import json 

# Clase para las pruebas unitarias
class TestPostModel(TestCase):
  
  #Setup
  #------------------------------------------------------
  def setUp(self):
    self.testPost = Post.objects.create(
      title = 'Título aquí',
      body = 'Cuerpo aquí'
    )

  #Pruebas para el modelo (Post)
  #------------------------------------------------------
  def test_title (self):
    print("titulo")
    title = 'Título aquí'
    self.assertEquals(self.testPost.title, title)

  def test_body (self):
    print("cuerpo")
    text = 'Cuerpo aquí'
    self.assertEquals(self.testPost.body, text)

  def test_created_at(self):
    self.assertIsNotNone(self.testPost.created_at)

  #Pruebas para las URL's
  #------------------------------------------------------
  def test_url_index(self):
    url = reverse('index')
    self.assertEquals(resolve(url).func, index)

  def test_url_post(self):
    url = reverse('post', args=[self.testPost.pk])
    self.assertEquals(resolve(url).func, post)


  #Pruebas para las vistas
  #------------------------------------------------------
  def test_index_GET(self):
    client = Client()
    response = client.get(reverse('index'))
    self.assertEquals(response.status_code, 200)

  def test_index_template(self):
    client = Client()
    response = client.get(reverse('index'))
    self.assertTemplateUsed(response, 'index.html')

  def test_post_GET(self):
    client = Client()
    response = client.get(reverse('post', args=[self.testPost.pk]))
    self.assertEquals(response.status_code, 200)

  def test_post_template(self):
    client = Client()
    response = client.get(reverse('post', args=[self.testPost.pk]))
    self.assertTemplateUsed(response, 'posts.html')

  def test_post_POST(self):
    
