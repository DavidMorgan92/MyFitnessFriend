from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, ProductVariant
from django.contrib.messages import get_messages


class AddToBasketTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_product = Product.objects.create(name='Test Product', price_pounds=10, category=Product.Category.OTHER)
        self.black_colour_variant = ProductVariant.objects.create(product=self.test_product, name='Black', type='Colour', price_pounds=10)
        self.grey_colour_variant = ProductVariant.objects.create(product=self.test_product, name='Grey', type='Colour', price_pounds=10)

    def test_returns_404_if_product_not_found(self):
        response = self.client.post(reverse('store_add_to_basket', args=[1001]))
        self.assertEqual(response.status_code, 404)

    def test_returns_400_if_post_data_is_missing_a_variant_value(self):
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]))
        self.assertEqual(response.status_code, 400)

    def test_returns_400_if_variant_value_does_not_exist(self):
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]), {
            'variant-Colour': 1001,
        })
        self.assertEqual(response.status_code, 400)

    def test_adds_new_item_to_basket(self):
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]), {
            'variant-Colour': self.black_colour_variant.id,
        })
        self.assertRedirects(response, reverse('store_details', args=[self.test_product.id]))
        self.assertEqual(len(self.client.session['basket']), 1)
        self.assertDictEqual(self.client.session['basket'][0], {
            'product_id': self.test_product.id,
            'count': 1,
            'variants': {
                'Colour': self.black_colour_variant.id,
            },
        })
    
    def test_adds_message_when_product_added(self):
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]), {
            'variant-Colour': self.black_colour_variant.id,
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].extra_tags, '')
        self.assertEqual(messages[0].level, 20)
        self.assertEqual(messages[0].level_tag, 'info')
        self.assertEqual(messages[0].message, 'Added Test Product to basket')
        self.assertEqual(messages[0].tags, 'info')

    def test_adds_count_to_existing_item(self):
        session = self.client.session
        session['basket'] = [
            {
                'product_id': self.test_product.id,
                'count': 1,
                'variants': {
                    'Colour': self.black_colour_variant.id,
                },
            },
        ]
        session.save()
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]), {
            'variant-Colour': self.black_colour_variant.id,
        })
        self.assertRedirects(response, reverse('store_details', args=[self.test_product.id]))
        self.assertEqual(len(self.client.session['basket']), 1)
        self.assertDictEqual(self.client.session['basket'][0], {
            'product_id': self.test_product.id,
            'count': 2,
            'variants': {
                'Colour': self.black_colour_variant.id,
            },
        })
    
    def test_counts_as_different_item_if_variant_value_is_different(self):
        session = self.client.session
        session['basket'] = [
            {
                'product_id': self.test_product.id,
                'count': 1,
                'variants': {
                    'Colour': self.black_colour_variant.id,
                },
            },
        ]
        session.save()
        response = self.client.post(reverse('store_add_to_basket', args=[self.test_product.id]), {
            'variant-Colour': self.grey_colour_variant.id,
        })
        self.assertRedirects(response, reverse('store_details', args=[self.test_product.id]))
        self.assertEqual(len(self.client.session['basket']), 2)
        self.assertDictEqual(self.client.session['basket'][0], {
            'product_id': self.test_product.id,
            'count': 1,
            'variants': {
                'Colour': self.black_colour_variant.id,
            },
        })
        self.assertDictEqual(self.client.session['basket'][1], {
            'product_id': self.test_product.id,
            'count': 1,
            'variants': {
                'Colour': self.grey_colour_variant.id,
            },
        })
