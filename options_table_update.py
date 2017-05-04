import sys
import requests
import settings
import constants
from college_data import COLLEGE_NAME_LIST
from company_data import COMPANY_NAME_LIST
from bike_data import BIKE_DATA
import time


def update_organisation_type(printing=False):
    url = settings.SERVER_URL + 'common/organisation_type/'
    if printing:
        for organisation_type_name in constants.ORGANISATION_TYPE:
            print requests.post(url, {"name": organisation_type_name, "is_active": True})
            # time.sleep(6)
    else:
        for organisation_type_name in constants.ORGANISATION_TYPE:
            requests.post(
                url, {"name": organisation_type_name, "is_active": True})
            # time.sleep(6)


def update_salary_payment_type(printing=False):
    url = settings.SERVER_URL + 'common/salary_payment_mode/'
    if printing:
        for salary_payment_type in constants.SALARY_PAYMENT_TYPE:
            print requests.post(url, {"name": salary_payment_type, "is_active": True})
            # time.sleep(6)
    else:
        for salary_payment_type in constants.SALARY_PAYMENT_TYPE:
            requests.post(
                url, {"name": salary_payment_type, "is_active": True})
            # time.sleep(6)


def update_borrower_type(printing=False):
    url = settings.SERVER_URL + 'participant/borrower_type/'
    if printing:
        for borrower_type_data in constants.BORROWER_TYPE:
            print requests.post(url, borrower_type_data)
            # time.sleep(6)
    else:
        for borrower_type_data in constants.BORROWER_TYPE:
            requests.post(url, borrower_type_data)
            # time.sleep(6)


def document_type(printing=False):
    url = settings.SERVER_URL + 'customer/document_type/'
    if printing:
        for document_type_data in constants.DOCUMENT_TYPE:
            print requests.post(url, document_type_data)
            # time.sleep(6)
    else:
        for document_type_data in constants.DOCUMENT_TYPE:
            requests.post(url, document_type_data)
            # time.sleep(6)


def profession_type(printing=False):
    url = settings.SERVER_URL + 'common/profession_type/'
    if printing:
        for profession_type_data in constants.PROFESSION_TYPE:
            print requests.post(url, {"type_name": profession_type_data, "is_active": True})
            # time.sleep(6)
    else:
        for profession_type_data in constants.PROFESSION_TYPE:
            requests.post(
                url, {"type_name": profession_type_data, "is_active": True})
            # time.sleep(6)


def lender(printing=False):
    url = settings.SERVER_URL + 'participant/lender/'
    if printing:
        for lender_data in constants.LENDER:
            print requests.post(url, lender_data)
            # time.sleep(6)
    else:
        for lender_data in constants.LENDER:
            requests.post(url, lender_data)
            # time.sleep(6)


def update_college(printing=False):
    url = settings.SERVER_URL + 'common/college/'
    if printing:
        for college_name in COLLEGE_NAME_LIST:
            print requests.post(url, {"name": college_name, "is_active": True})
            # time.sleep(6)
    else:
        for college_name in COLLEGE_NAME_LIST:
            requests.post(
                url, {"name": college_name, "is_active": True})
            # time.sleep(6)


def update_company(printing=False):
    url = settings.SERVER_URL + 'common/company/'
    if printing:
        for company_name in COMPANY_NAME_LIST:
            print requests.post(url, {"name": company_name, "is_active": True})
            # time.sleep(6)
    else:
        for company_name in COMPANY_NAME_LIST:
            requests.post(
                url, {"name": company_name, "is_active": True})
            # time.sleep(6)


def update_loan_purpose(printing=False):
    url = settings.SERVER_URL + 'common/loan_purpose/'
    if printing:
        for loan_purpose in constants.LOAN_PURPOSE:
            print requests.post(url, {"name": loan_purpose, "is_active": True})
            # time.sleep(6)
    else:
        for loan_purpose in constants.LOAN_PURPOSE:
            requests.post(
                url, {"name": loan_purpose, "is_active": True})
            # time.sleep(6)


def bike_data(printing=False):
    url = settings.SERVER_URL + 'common/bike/'
    if printing:
        for bike_data in BIKE_DATA:
            minimum = bike_data.pop('min')
            maximum = bike_data.pop('max')
            bike_data['approximate_price'] = minimum
            bike_data['down_payment'] = int(0.2 * minimum)
            bike_data['is_active'] = True
            print requests.post(url, bike_data)
            # time.sleep(6)
    else:
        for bike_data in BIKE_DATA:
            minimum = bike_data.pop('min')
            maximum = bike_data.pop('max')
            bike_data['approximate_price'] = minimum
            bike_data['down_payment'] = int(0.2 * minimum)
            bike_data['is_active'] = True
            # time.sleep(6)
if __name__ == '__main__':

    run_all = sys.argv[1]

    if run_all:
        print "Updating tables: organisation_type, salary_payment_type, borrower_type, document_type, loan_type,lender"
        update_organisation_type()
        update_salary_payment_type()
        update_borrower_type()
        document_type()
        loan_type()
        lender()
        update_college()
        update_company()
        print "Update all the tables"
    else:
        print "To Run all Provide Non Zero Value as Script Argument"
