ORGANISATION_TYPE = [
    "Government",
    "Public Sector Undertaking",
    "Public Limited Company",
    "Private Limited Company",
    "Partner - Partnership Form",
    "Proprietor - Proprietor Form",
    "Self Employed Professional (Non-Registered Entity)",
]


SALARY_PAYMENT_TYPE = [
    "Cash",
    "Online",
    "Cheque"
]

BORROWER_TYPE = [
    {
        "is_active": True,
        "type_name": "standard",
        "max_current_loans_allowed": 1
    }
]

DOCUMENT_TYPE = [
    {
        "name": "profile_pic",
        "usage": "KYC purpose"
    },
    {
        "name": "aadhaar",
        "usage": "KYC purpose"
    },
    {
        "name": "pan",
        "usage": "KYC purpose"
    },
    {
        "name": "salary_slips",
        "usage": "Eligibility Purpose"
    },
    {
        "name": "address_proof",
        "usage": "KYC purpose"
    },
    {
        "name": "unsigned_loan_agreement",
        "usage": "KYC purpose"
    },
    {
        "name": "signed_loan_agreement",
        "usage": "KYC purpose"
    }
]

LOAN_TYPE = [
    {
        "is_active": True,
        "type_name": "Bullet",
        "one_time_processing_fee": "3.0000",
        "number_of_repayment_cycles": 1,
        "accounting_days_in_cycle": 30,
        "calender_days_in_cycle": 30,
        "repayment_type": "installments",
        "interest_rate_per_day": "0.0666",
        "interest_rate_type": "momrb",
        "is_processing_fee_deducted_at_source": True,
        "is_interest_deducted_at_source": True,
        "penalty_amount_per_cycle": 500,
        "penalty_percent_per_cycle": None
    }
]

LENDER = [
    {
        "is_active": True,
        "name": "Swastika",
        "lender_type": "nbfc",
        "allocation_limit": 200000
    }
]

LOAN_PURPOSE = [
    "Two-Wheeler",
    "Mobile",
    "Home Construction, Renovation etc.",
    "Family Function, Marriage etc.",
    "Other"
]

PROFESSION_TYPE = [
    "Retail Sales Associate",
    "Account Assistant",
    "BPO/Back Office Executive",
    "Content Writer/Digital Marketing",
    "Delivery Boy",
    "Driver",
    "Electrician/Plumber/Carpenter/Mechanic",
    "Field Executive (Banks, BFSI etc.)",
    "Housekeeping/Facility Management",
    "Nurse/Caregiver/Physio",
    "Office Boy/Govt. Peon",
    "Retail Shop Owner/Business Owner",
    "Business Development/Promo Staff",
    "Security Guard",
    "Telesales/Telemarketing",
    "Others", "Factory Worker",
    "Beautician/Salon Worker",
    "Restaurant Staff",
    "Hotel Staff",
    "Others,"
]
