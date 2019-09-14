from unittest import TestCase
from com.Guilherme.num_div import Operacoes

class TestOperacoes(TestCase):
    def setUp(self):
        self.num_div = Operacoes()

    
    def test_num_div(self):
        assert Operacoes.num_div(20,10)

