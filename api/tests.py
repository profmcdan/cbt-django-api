from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from .models import BucketList
# Create your tests here.


class BucketListModelTestCase(TestCase):
    """ This class defines the test for Bucketlist Test """

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = BucketList(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'), self.bucketlist_data, format='json')

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details', kwargs={"pk": bucketlist.id}), format='jsom')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        change_bucketlist = {'name': "Something new"}
        bucketlist = BucketList.objects.get()
        res = self.client.put(reverse(
            'details', kwargs={'pk': bucketlist.id}), change_bucketlist, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = BucketList.objects.get()
        res = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}), format='json', follow=True)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
