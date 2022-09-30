import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_AssertIsNot(unittest.TestCase):
 def test1(self):
  materia = "Testing Software";
  # Verificar valores
  self.assertIsNot(materia, "Ingenieria de Software","No son iguales")

if __name__ =="__main__":
 unittest.main()


class Test_AssertIsNotNone(unittest.TestCase):
 def test(self):
  materia = "Testing Software";
  # Verificar valores
  self.assertIsNotNone(materia, "La materia no está en nulo")

if __name__ =="__main__":
 unittest.main()

class test_case1(unittest.TestCase):
 def test1(self):
  sitio1 = "Uniempresarial"
  sitio2 = "Cámara de comercio de Bogotá"
  # Verificar valores
  self.assertTrue(sitio1 == sitio2, "No son iguales")

if __name__ =="__main__":
 unittest.main()

class Test_AssertEqual(unittest.TestCase):
 def validarsteam(self):
     driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver.exe')
     driver.get('https://store.steampowered.com')
     Steam = driver.title
     Steam2 = ("home - Steam")
     #validad información del titulo de la pagina de steam
     self.assertEqual(Steam, Steam2,"Titulos de páginas diferentes")

if __name__ =="__main__":
 unittest.main()
