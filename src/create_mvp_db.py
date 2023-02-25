import httpx
from tests.endpoints.data import company_data


print('Start create MVP database...')

url = 'http://127.0.0.1:8000/api/v1/company/'
for data in company_data.create_company_valid:
    response = httpx.post(url=url, data=data)
    print('------------',response)

print('MVP database was creaded.')
