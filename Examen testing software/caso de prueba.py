import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

class suite(unittest.TestCase):
    def caso_de_prueba(self):
        self.cdriver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver.exe')
        self.cdriver = webdriver.Ie(executable_path=r'C:\JoseDanilo\Python\chromedriver.exe')

    def test_busqueda(self):
        self.cdriver.get("https://www.google.com/")
        self.busqueda = self.cdriver.find_element_by_name("q")
        self.busqueda.submit("selenium")
        time.sleep(2)

    def test_busqueda(self):
        self.cdriver.get("https://tlauncher.org/en/")
        time.sleep(2)
        self.cdriver.execute_script("window.scrollTo(0,document.body.scrollHeight")
        time.sleep(2)
        
    def tearDown(self):
        self.cedriver.quit()
        self.cdriver.quit()
        
        if __name__ == '__main__':
            unittest.main()

        driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
        driver.get('file:///C:\JoseDanilo\Python\a.html')
        email = driver.find_element(By.NAME,"email")
        print("Email ", email)




        
class Test_AssertIsNotNone(unittest.TestCase):
 def testdevalidación(self):
  control = ("Xbox")
  # Verificar valores
  self.assertIsNotNone(control, "si es igual aXbox")
if __name__ =="__main__":
 unittest.main()


class test_case1(unittest.TestCase):
 def test1(self):
  sitio1 = "netflix"
  sitio2 = "primevideo"
  # Verificar valores
  self.assertTrue(sitio1 == sitio2, "No son iguales")
if __name__ =="__main__":
 unittest.main()
