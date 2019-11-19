from selenium.webdriver.common.by import By


class Locators(object):
    LETTER = (
        By.CSS_SELECTOR, '#ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_lnkCaracterA')
    FRAME = (By.ID, 'bvmf_iframe')
    TRBODY = (By.XPATH, '//tbody/tr[1]')
    REPORTS = (By.XPATH, '//span[text()= "Relatórios Estruturados"]')
    DOC = (By.ID, 'ctl00_contentPlaceHolderConteudo_rptDocumentosITR_ctl00_lnkDocumento')
