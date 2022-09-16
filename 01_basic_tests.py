import requests


def test_get_info_check_status_code_equals_200(info_url):
    response = requests.get(info_url)
    assert response.status_code == 200


def test_get_info_check_content_type_equals_json(info_url):
    response = requests.get(info_url)
    assert response.headers['Content-Type'] == "application/json"


def test_get_info_check_product_name_equals_dexcom_api(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    assert response_body[0]["Product Name"] == "Dexcom API"

def test_get_info_check_UDI_device_identifier_equals_00386270000668(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    assert response_body[0]["UDI / Device Identifier"] == "00386270000668"

def test_get_info_check_UDI_production_identifier_version_3110(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    assert response_body[0]["UDI / Production Identifier"]["Version"] == "3.1.1.0"

def test_get_info_check_UDI_production_identifier_part_number_350_0019(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    assert response_body[0]["UDI / Production Identifier"]["Part Number (PN)"] == "350-0019"

def test_get_info_check_UDI_production_identifier_SubComponents_Name_api_gateway(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    assert response_body[0]["UDI / Production Identifier"]["Sub-Components"][0]["Name"] == "api-gateway"

def test_get_info_check_UDI_production_identifier_SubComponents_Name_insulin_service(info_url):
    response = requests.get(info_url)
    response_body = response.json()
    inx = len(response_body)
    found = 0
    for i in range(0,inx):
        ins = len(response_body[i]["UDI / Production Identifier"]["Sub-Components"])
        for j in range(0,ins):
            if response_body[i]["UDI / Production Identifier"]["Sub-Components"][j]["Name"] == "insulin-service" :
                found = 1
                break
    
    assert found == 0

def test_get_info_check_content_type_equals_xml(info_url):
    response = requests.get(info_url)
    assert response.headers['Content-Type'] == "application/xml"

def test_get_info_api(info_url):
    print("testing the url :" + info_url)
    test_get_info_check_status_code_equals_200(info_url)
    test_get_info_check_content_type_equals_json(info_url)
    test_get_info_check_product_name_equals_dexcom_api(info_url)
    test_get_info_check_UDI_device_identifier_equals_00386270000668(info_url)
    test_get_info_check_UDI_production_identifier_version_3110(info_url)
    test_get_info_check_UDI_production_identifier_part_number_350_0019(info_url)
    test_get_info_check_UDI_production_identifier_SubComponents_Name_api_gateway(info_url)
    test_get_info_check_UDI_production_identifier_SubComponents_Name_insulin_service(info_url)
    test_get_info_check_content_type_equals_xml(info_url)


def main():
    info_url = "https://api.dexcom.com/info"
    test_get_info_api(info_url)
    sandbox_info_url = "https://sandbox-api.dexcom.com/info"
    test_get_info_api(sandbox_info_url)
    
    
if __name__ == "__main__":
         main()