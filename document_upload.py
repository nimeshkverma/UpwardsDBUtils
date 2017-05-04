import requests


def create_test_file(path):
    f = open(path, 'rb')
    return f


def upload_file(customer_id, url, token):
    requests_headers = {
        'Session-Token': token
    }
    requests_data = {
        "customer_id": customer_id,
        "document_type_id": 1,
        "status": "uploaded",
    }
    requests_files = {
        "document_1": create_test_file('test_image1.jpg'),
        "document_2": create_test_file('test_image2.jpg'),
    }
    response = requests.post(
        url, headers=requests_headers, files=requests_files, data=requests_data)
    print response, response.text
    return response


def update_file(customer_id, url, token):
    requests_headers = {
        'Session-Token': token
    }
    requests_data = {
        "customer_id": customer_id,
        "document_type_id": 1,
        "status": "uploaded",
    }
    requests_files = {
        "document_1": create_test_file('test_image2.jpg'),
        "document_2": create_test_file('test_image1.jpg'),
    }
    response = requests.put(
        url, headers=requests_headers, files=requests_files, data=requests_data)
    print response, response.text
    return response


def delete_filte(customer_id, url, token):
    requests_headers = {
        'Session-Token': token
    }
    requests_data = {
        "customer_id": customer_id,
        "document_type_id": 1,
        "status": "uploaded",
    }
    response = requests.delete(
        url, headers=requests_headers, data=requests_data)
    print response, response.text
    return response
