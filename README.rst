.. image:: https://img.shields.io/pypi/v/netsgiro.svg?style=flat
    :target: https://pypi.org/project/netsgiro/
    :alt: Latest PyPI version

.. image:: https://github.com/otovo/python-avtalegiro/actions/workflows/test.yml/badge.svg
    :target: https://github.com/otovo/python-avtalegiro/actions/workflows/test.yml
    :alt: Github actions test pipeline status

.. image:: https://img.shields.io/readthedocs/netsgiro.svg
   :target: https://netsgiro.readthedocs.io/
   :alt: Read the Docs build status

.. image:: https://img.shields.io/codecov/c/github/netsgiro/python-avtalegiro/master.svg
   :target: https://codecov.io/gh/netsgiro/python-avtalegiro
   :alt: Test coverage

========
avtalegiro
========

avtalegiro is a Python library for working with `Avtalegiro <https://www.avtalegiro.no/>`_
AvtaleGiro and OCR Giro files.

AvtaleGiro is a direct debit solution that is in widespread use in Norway, with
more than 15 000 companies offering it to their customers. OCR Giro is used by
Nets and Norwegian banks to update payees on recent deposits to their bank
accounts. In combination, AvtaleGiro and OCR Giro allows for a high level of
automation of invoicing and payment processing.

The avtalegiro library supports:

- Parsing AvtaleGiro agreements
- Creating AvtaleGiro payment requests
- Creating AvtaleGiro cancellations
- Parsing OCR Giro transactions

netsgiro is available from PyPI. To install it, run::

    pip install netsgiro

For details and code examples, see `the netsgiro documentation
<https://netsgiro.readthedocs.io/>`_.

For further details, please refer to the official
`AvtaleGiro <https://www.avtalegiro.no/>`_ and
`OCR Giro <https://www.mastercardpaymentservices.com>`_
documentation from Nets.


License
=======

Copyright 2017-2019 `Otovo AS <https://www.otovo.com/>`_. Licensed under the
Apache License, Version 2.0. See the ``LICENSE`` file for the full license
text.


Project resources
=================

- `Documentation <https://netsgiro.readthedocs.io/>`_
- `Source code <https://github.com/zensum/python-avtalegiro>`_
- `Issue tracker <https://github.com/zensum/python-avtalegiro/issues>`_
