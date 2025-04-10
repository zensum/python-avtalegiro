from datetime import date

import pytest

import avtalegiro
from avtalegiro.objects import Transmission
from avtalegiro.records import AssignmentEnd


@pytest.fixture
def transmission():
    return avtalegiro.Transmission(
        number='0000001',
        data_transmitter='12341234',
        data_recipient=avtalegiro.NETS_ID,
        date=date(2004, 6, 17),
    )


def test_transmission_from_zero_records_fails():
    with pytest.raises(ValueError, match='At least 2 records required, got 0'):
        avtalegiro.Transmission.from_records([])


def test_assignment_from_zero_records_fails():
    with pytest.raises(ValueError, match='At least 2 records required, got 0'):
        avtalegiro.Assignment.from_records([])


def test_transmission__get_assignments_validation():
    assignment_end = AssignmentEnd.from_string(
        'NY210088000000060000002000000000000000600170604170604000000000000000000000000000'
    )

    # Check that we fail if the first item is not an `AssignmentStart` instance
    for item in ['test', assignment_end]:
        with pytest.raises(ValueError, match='Expected AssignmentStart record, got '):
            Transmission._get_assignments([item])
