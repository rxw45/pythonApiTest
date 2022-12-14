import requests
import pytest
import csv

info_url = "https://api.dexcom.com/info"
sandbox_info_url = "https://sandbox-api.dexcom.com/info"

test_data_info_api_level1 = [
    (info_url,0,"Product Name", "Dexcom API"),
    (info_url,0, "UDI / Device Identifier", "00386270000668"),
    (sandbox_info_url,0,"Product Name", "Dexcom API"),
    (sandbox_info_url,0, "UDI / Device Identifier", "00386270000668")        
]

test_data_info_api_level2 = [
    (info_url,0,"UDI / Production Identifier", "Version","3.1.1.0"),
    (info_url,0, "UDI / Production Identifier", "Part Number (PN)","350-0019"),
    (sandbox_info_url,0,"UDI / Production Identifier", "Version","3.1.1.0"),
    (sandbox_info_url,0, "UDI / Production Identifier", "Part Number (PN)","350-0019")    
]

test_data_info_api_level3 = [
    (info_url,0,"UDI / Production Identifier", "Sub-Components","Name","api-gateway"),
    (sandbox_info_url,0,"UDI / Production Identifier", "Sub-Components","Name","api-gateway") 
]


@pytest.mark.parametrize("url, index, field,expected_value", test_data_info_api_level1)
def test_using_level1_data_get_info_check_expected_value(url, index, field, expected_value):
    response = requests.get(url)
    response_body = response.json()
    assert response_body[index][field] == expected_value

@pytest.mark.parametrize("url, index, field1, field2 ,expected_value", test_data_info_api_level2)
def test_using_level2_data_get_info_check_expected_value(url, index, field1, field2, expected_value):
    response = requests.get(url)
    response_body = response.json()
    assert response_body[index][field1][field2] == expected_value

@pytest.mark.parametrize("url, index, field1, field2 , field3,expected_value", test_data_info_api_level3)
def test_using_level3_data_get_info_check_expected_value(url, index, field1, field2, field3,expected_value):
    response = requests.get(url)
    response_body = response.json()
    assert response_body[index][field1][field2][0][field3] == expected_value


 







