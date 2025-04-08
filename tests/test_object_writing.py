import avtalegiro


def test_write_agreements(agreements_data):
    transmission = avtalegiro.parse(agreements_data)

    result = transmission.to_ocr()

    assert result == agreements_data.strip()


def test_write_payment_request(payment_request_data):
    transmission = avtalegiro.parse(payment_request_data)

    result = transmission.to_ocr()

    assert result == payment_request_data.strip()


def test_write_ocr_giro_transactions(ocr_giro_transactions_data):
    transmission = avtalegiro.parse(ocr_giro_transactions_data)

    result = transmission.to_ocr()

    assert result == ocr_giro_transactions_data.strip()
