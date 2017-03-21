import sys
import requests
import settings
import constants


def update_organisation_type(printing=False):
    url = settings.SERVER_URL + 'common/organisation_type/'
    if printing:
        for organisation_type_name in constants.ORGANISATION_TYPE:
            print requests.post(url, {"name": organisation_type_name, "is_active": True})
    else:
        for organisation_type_name in constants.ORGANISATION_TYPE:
            requests.post(
                url, {"name": organisation_type_name, "is_active": True})


def update_salary_payment_type(printing=False):
    url = settings.SERVER_URL + 'common/salary_payment_mode/'
    if printing:
        for salary_payment_type in constants.SALARY_PAYMENT_TYPE:
            print requests.post(url, {"name": salary_payment_type, "is_active": True})
    else:
        for salary_payment_type in constants.SALARY_PAYMENT_TYPE:
            requests.post(
                url, {"name": salary_payment_type, "is_active": True})


def update_borrower_type(printing=False):
    url = settings.SERVER_URL + 'participant/borrower_type/'
    if printing:
        for borrower_type_data in constants.BORROWER_TYPE:
            print requests.post(url, borrower_type_data)
    else:
        for borrower_type_data in constants.BORROWER_TYPE:
            requests.post(url, borrower_type_data)


def document_type(printing=False):
    url = settings.SERVER_URL + 'customer/document_type/'
    if printing:
        for document_type_data in constants.DOCUMENT_TYPE:
            print requests.post(url, document_type_data)
    else:
        for document_type_data in constants.DOCUMENT_TYPE:
            requests.post(url, document_type_data)


def loan_type(printing=False):
    url = settings.SERVER_URL + 'loan/type/'
    if printing:
        for loan_type_data in constants.LOAN_TYPE:
            print requests.post(url, loan_type_data)
    else:
        for loan_type_data in constants.LOAN_TYPE:
            requests.post(url, loan_type_data)


def lender(printing=False):
    url = settings.SERVER_URL + 'loan/type/'
    if printing:
        for lender_data in constants.LENDER:
            print requests.post(url, lender_data)
    else:
        for lender_data in constants.LENDER:
            requests.post(url, lender_data)

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
        print "Update all the tables"
    else:
        print "To Run all Provide Non Zero Value as Script Argument"
