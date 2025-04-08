from datetime import date

import pytest

import avtalegiro
import avtalegiro.records


def test_parse_with_too_short_lines_fails():
    with pytest.raises(ValueError, match='exactly 80 chars long'):
        avtalegiro.records.parse('NY0000\nNY0000\n')


def test_parse_with_nonnumeric_record_type():
    with pytest.raises(ValueError, match="Record type must be numeric, got 'AA'"):
        avtalegiro.records.parse('NY0000AA' + '0' * 72)


def test_parse_with_unknown_record_type():
    with pytest.raises(ValueError, match='99 is not a valid RecordType'):
        avtalegiro.records.parse('NY000099' + '0' * 72)


def test_parse_avtalegiro_agreements(agreements_data):
    result = avtalegiro.records.parse(agreements_data)

    assert len(result) == 20

    transmission_start = result[0]
    assignment_start = result[1]
    agreement_1 = result[2]
    agreement_2 = result[3]
    assignment_end = result[-2]
    transmission_end = result[-1]

    assert isinstance(transmission_start, avtalegiro.records.TransmissionStart)
    assert transmission_start.transmission_number == '1091949'
    assert transmission_start.data_transmitter == avtalegiro.NETS_ID

    assert isinstance(assignment_start, avtalegiro.records.AssignmentStart)
    assert assignment_start.assignment_account == '99991042764'

    assert isinstance(agreement_1, avtalegiro.records.AvtaleGiroAgreement)
    assert agreement_1.registration_type == (
        avtalegiro.AvtaleGiroRegistrationType.NEW_OR_UPDATED_AGREEMENT
    )
    assert agreement_1.kid == '000112000507155'
    assert agreement_1.notify is True

    assert isinstance(agreement_2, avtalegiro.records.AvtaleGiroAgreement)
    assert agreement_2.registration_type == (
        avtalegiro.AvtaleGiroRegistrationType.NEW_OR_UPDATED_AGREEMENT
    )
    assert agreement_2.kid == '001006300507304'
    assert agreement_2.notify is False

    assert isinstance(assignment_end, avtalegiro.records.AssignmentEnd)
    assert assignment_end.num_transactions == 16
    assert assignment_end.num_records == 18
    assert assignment_end.total_amount is None
    assert assignment_end.nets_date_earliest is None
    assert assignment_end.nets_date_latest is None

    assert isinstance(transmission_end, avtalegiro.records.TransmissionEnd)
    assert transmission_end.num_transactions == 16
    assert transmission_end.num_records == 20
    assert transmission_end.total_amount == 0
    assert transmission_end.nets_date == date(2017, 4, 19)


def test_parse_avtalegiro_payment_requests(payment_request_data):
    result = avtalegiro.records.parse(payment_request_data)

    assert len(result) == 22

    transmission_start = result[0]
    assignment_start = result[1]
    transaction_amount_1 = result[2]
    transaction_amount_2 = result[3]
    transaction_spec_1 = result[4]
    transaction_spec_2 = result[5]
    assignment_end = result[-2]
    transmission_end = result[-1]

    assert isinstance(transmission_start, avtalegiro.records.TransmissionStart)
    assert transmission_start.transmission_number == '1000081'
    assert transmission_start.data_recipient == avtalegiro.NETS_ID

    assert isinstance(assignment_start, avtalegiro.records.AssignmentStart)
    assert assignment_start.assignment_account == '88888888888'

    assert isinstance(transaction_amount_1, avtalegiro.records.TransactionAmountItem1)
    assert transaction_amount_1.nets_date == date(2004, 6, 17)
    assert transaction_amount_1.amount == 100
    assert transaction_amount_1.kid == '008000011688373'

    assert isinstance(transaction_amount_2, avtalegiro.records.TransactionAmountItem2)
    assert transaction_amount_2.payer_name == 'NAVN'
    assert transaction_amount_2.reference is None

    assert isinstance(transaction_spec_1, avtalegiro.records.TransactionSpecification)
    assert transaction_spec_1.text == ' Gjelder Faktura: 168837  Dato: 19/03/04'

    assert isinstance(transaction_spec_2, avtalegiro.records.TransactionSpecification)
    assert transaction_spec_2.text == '                  ForfallsDato: 17/06/04'

    assert isinstance(assignment_end, avtalegiro.records.AssignmentEnd)
    assert assignment_end.num_transactions == 6
    assert assignment_end.num_records == 20
    assert assignment_end.total_amount == 600
    assert assignment_end.nets_date_earliest == date(2004, 6, 17)
    assert assignment_end.nets_date_latest == date(2004, 6, 17)

    assert isinstance(transmission_end, avtalegiro.records.TransmissionEnd)
    assert transmission_end.num_transactions == 6
    assert transmission_end.num_records == 22
    assert transmission_end.total_amount == 600
    assert transmission_end.nets_date == date(2004, 6, 17)


def test_parse_ocr_giro_transactions(ocr_giro_transactions_data):
    result = avtalegiro.records.parse(ocr_giro_transactions_data)

    assert len(result) == 45

    transmission_start = result[0]
    assignment_start = result[1]
    transaction_amount_1 = result[2]
    transaction_amount_2 = result[3]
    transaction_amount_3 = result[4]
    assignment_end = result[-2]
    transmission_end = result[-1]

    assert isinstance(transmission_start, avtalegiro.records.TransmissionStart)
    assert transmission_start.transmission_number == '0170031'
    assert transmission_start.data_recipient == '00010200'

    assert isinstance(assignment_start, avtalegiro.records.AssignmentStart)
    assert assignment_start.assignment_account == '99991042764'

    assert isinstance(transaction_amount_1, avtalegiro.records.TransactionAmountItem1)
    assert transaction_amount_1.nets_date == date(1992, 1, 20)
    assert transaction_amount_1.amount == 102000
    assert transaction_amount_1.kid == '0000531'

    assert isinstance(transaction_amount_2, avtalegiro.records.TransactionAmountItem2)
    assert transaction_amount_2.payer_name is None
    assert transaction_amount_2.form_number == '9636827194'
    assert transaction_amount_2.reference == '099038562'
    assert transaction_amount_2.bank_date == date(1992, 1, 16)
    assert transaction_amount_2.debit_account == '99990512341'

    assert isinstance(transaction_amount_3, avtalegiro.records.TransactionAmountItem3)
    assert transaction_amount_3.text == 'Foo bar baz'

    assert isinstance(assignment_end, avtalegiro.records.AssignmentEnd)
    assert assignment_end.num_transactions == 20
    assert assignment_end.num_records == 43
    assert assignment_end.total_amount == 5144900
    assert assignment_end.nets_date == date(1992, 1, 20)
    assert assignment_end.nets_date_earliest == date(1992, 1, 20)
    assert assignment_end.nets_date_latest == date(1992, 1, 20)

    assert isinstance(transmission_end, avtalegiro.records.TransmissionEnd)
    assert transmission_end.num_transactions == 20
    assert transmission_end.num_records == 45
    assert transmission_end.total_amount == 5144900
    assert transmission_end.nets_date == date(1992, 1, 20)
