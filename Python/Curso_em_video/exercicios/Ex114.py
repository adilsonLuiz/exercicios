"""  
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""


def teste_connection(url):
    import urllib3
    site = urllib3.PoolManager()

    try:
        resp = site.request('GET', url)
    except urllib3.exceptions.MaxRetryError:
        print('Site inacesivel')
    except urllib3.exceptions.LocationValueError:
        print('Não foi possivel achar o host, verifique a URL digitada')
    else:
        print('Site acessivel')


def get_data_site(url):
    import urllib3

    site = urllib3.PoolManager()

    try:
        resp = site.request('GET', url)
    except urllib3.exceptions.MaxRetryError:
        print('Site inacesivel')
    except urllib3.exceptions.LocationValueError:
        print('Não foi possivel achar o host, verifique a URL digitada')
    else:
        return resp.data



site = str(input('Informe um site: '))
teste_connection(site)
print(get_data_site(site))