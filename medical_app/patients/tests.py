from django.test import TestCase
from django.urls import reverse
from .models import Patient, Examination
from django.contrib.auth.models import User


class PatientModelTestsCreate(TestCase):

    def test_patient_creation(self):
        patient = Patient.objects.create(
            first_name="Test",
            last_name="Johny",
            date_of_birth="2001-09-11"
        )
        self.assertEqual(patient.first_name, "Test")
        self.assertEqual(patient.last_name, "Johny")


class ExaminationModelTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Bloody",
            last_name="Marry",
            ##year/month/day
            date_of_birth="1558-08-17"
        )

    def test_examination_creation(self):
        examination = Examination.objects.create(
            patient=self.patient,
            description="Death",
            date="1558-09-16"
        )
        self.assertEqual(examination.description, "Death")
        self.assertEqual(examination.patient, self.patient)


class PatientViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_patient_list_view(self):
        # Test if the patient list page loads correctly
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/patient_list.html')

    def test_add_patient_view(self):
        response = self.client.post(reverse('add_patient'), {
            'first_name': 'Alice',
            'last_name': 'Brown',
            'date_of_birth': '2000-08-08'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after a successful add
        self.assertTrue(Patient.objects.filter(first_name="Alice").exists())


class IntegrationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpsw')
        self.client.login(username='testuser', password='testpsw')
        self.patient = Patient.objects.create(
            first_name="Maciej",
            last_name="Testowy",
            date_of_birth="2000-11-27"
        )

    def test_patient_and_examination_flow(self):
        # Test creating a new patient then adding examination
        response = self.client.post(reverse('add_patient'), {
            'first_name': 'Carol',
            'last_name': 'Johnson',
            'date_of_birth': '1992-11-11'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect on success

        patient = Patient.objects.get(first_name="Carol")

        response = self.client.post(reverse('add_examination', args=[patient.id]), {
            'description': 'Skin exam test',
            'date': '2024-02-15'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        self.assertTrue(Examination.objects.filter(patient=patient, description='Skin exam test').exists())


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpsw'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
