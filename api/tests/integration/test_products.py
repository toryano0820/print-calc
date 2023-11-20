from django.test import Client, TestCase, utils, override_settings


class TestProducts(TestCase):
    def setUp(self):
        # utils.setup_databases(1, False)
        pass

    def test_create_product_inserts_database_entry(self):
        response = self.client.post(
            "/api/products",
            json={"name": "test_product", "price": "1.0", "currency_symbol": "USD"}
        )
