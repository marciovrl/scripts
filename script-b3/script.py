from browser import Browser
from page import Page
from locators import Locators


browser = Browser().create_browser(browser='chrome')
locator = Locators()

page = Page(browser)

page.go_url(
    'http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?idioma=pt-br')

page.click(*locator.LETTER)
page.click(*locator.TRBODY)
page.click(*locator.REPORTS)

# page.sleep(50)
