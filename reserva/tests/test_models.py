from datetime import date

import pytest
from model_bakery import baker

from reserva.models import Reserva, Petshop

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada():
    data = date(2022, 8, 30)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='tarde'
    )

    assert str(reserva) == 'Tom: 2022-08-30 - tarde'

    @pytest.mark.django_db
    def test_qtd_reservas_deve_retornar_reservas():
        petshop = baker.make(Petshop)
        quantidade = 3
        baker.make(
            Reserva,
            quantidade,
            petshop=petshop
        )

        assert petshop.qtd_reservas() == 3
