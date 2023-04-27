from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year


class CourseInfoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester", email="test@email.com", password="{iSchoolUI}"
        )


class InstructorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.instructor = Instructor.objects.create(
            first_name="Kevin", last_name="Trainor", disambiguator="",
        )

    def test_instructor_model(self):
        self.assertEqual(self.instructor.first_name, "Kevin")
        self.assertEqual(self.instructor.last_name, "Trainor")
        self.assertEqual(self.instructor.disambiguator, "")
        self.assertEqual(self.post.get_absolute_url(), "/instructor")

    def test_url_exists_at_correct_location_instructor_list_view(self):
        response = self.client.get("/instructor")
        self.assertEqual(response.status_code, 200)

    def test_instructor_list_view(self):
        response = self.client.get(reverse("instructor"))
        no_response = self.client.get("/instructor")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Kevin")
        self.assertContains(response, "Trainor")
        self.assertContains(response, "")
        self.assertTemplateUsed(response, "instructor_list.html")


class SectionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.section = Section.objects.create(
            section_name="AOG", course_id="IS439 - Web Development", instructor_id="Kevin", semester_id="2023 - Spring",
        )

    def test_section_model(self):
        self.assertEqual(self.section.section_name, "AOG")
        self.assertEqual(self.section.course_id, "IS439 - Web Development")
        self.assertEqual(self.section.semester_id, "2023 - Spring")
        self.assertEqual(self.section.instructor_id, "Kevin")
        self.assertEqual(self.post.get_absolute_url(), "/section")

    def test_url_exists_at_correct_location_section_list_view(self):
        response = self.client.get("/section")
        self.assertEqual(response.status_code, 200)

    def test_section_list_view(self):
        response = self.client.get(reverse("section"))
        no_response = self.client.get("/section")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "AOG")
        self.assertContains(response, "IS439 - Web Development")
        self.assertContains(response, "2023 - Spring")
        self.assertContains(response, "Kevin")
        self.assertTemplateUsed(response, "section_list.html")


class CourseTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course = Course.objects.create(
            course_number="IS439", course_name="Web Development",
        )

    def test_course_model(self):
        self.assertEqual(self.course.course_number, "IS439")
        self.assertEqual(self.course.course_name, "Web Development")
        self.assertEqual(self.post.get_absolute_url(), "/course")

    def test_url_exists_at_correct_location_course_list_view(self):
        response = self.client.get("/course")
        self.assertEqual(response.status_code, 200)

    def test_course_list_view(self):
        response = self.client.get(reverse("course"))
        no_response = self.client.get("/course")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "IS439")
        self.assertContains(response, "Web Development")
        self.assertTemplateUsed(response, "course_list.html")


class SemesterTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.semester = Semester.objects.create(
            period_id="Spring", year_id="2023",
        )

    def test_semester_model(self):
        self.assertEqual(self.semester.period_id, "Spring")
        self.assertEqual(self.semester.year_id, "2023")
        self.assertEqual(self.post.get_absolute_url(), "/semester")

    def test_url_exists_at_correct_location_semester_list_view(self):
        response = self.client.get("/semester")
        self.assertEqual(response.status_code, 200)

    def test_semester_list_view(self):
        response = self.client.get(reverse("semester"))
        no_response = self.client.get("/semester")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Spring")
        self.assertContains(response, "2023")
        self.assertTemplateUsed(response, "semester_list.html")


class StudentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(
            first_name="Sanjana", last_name="Dash", disambiguator="",
        )

    def test_student_model(self):
        self.assertEqual(self.student.first_name, "Sanjana")
        self.assertEqual(self.student.last_name, "Dash")
        self.assertEqual(self.student.disambiguator, "")
        self.assertEqual(self.post.get_absolute_url(), "/student")

    def test_url_exists_at_correct_location_student_list_view(self):
        response = self.client.get("/student")
        self.assertEqual(response.status_code, 200)

    def test_student_list_view(self):
        response = self.client.get(reverse("student"))
        no_response = self.client.get("/student")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Sanjana")
        self.assertContains(response, "Dash")
        self.assertContains(response, "")
        self.assertTemplateUsed(response, "student_list.html")


class RegistrationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.registration = Registration.objects.create(
            section_id="IS439 - AOG (Spring 2023)", student_id="Sanjana Dash",
        )

    def test_registration_model(self):
        self.assertEqual(self.registration.section_id, "IS439 - AOG (Spring 2023)")
        self.assertEqual(self.registration.student_id, "Sanjana Dash")
        self.assertEqual(self.post.get_absolute_url(), "/registration")

    def test_url_exists_at_correct_location_registration_list_view(self):
        response = self.client.get("/registration")
        self.assertEqual(response.status_code, 200)

    def test_registration_list_view(self):
        response = self.client.get(reverse("registration"))
        no_response = self.client.get("/registration")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "IS439 - AOG (Spring 2023)")
        self.assertContains(response, "Sanjana Dash")
        self.assertTemplateUsed(response, "registration_list.html")

        # cls.period = Period.objects.create(
        #     period_sequence="1", period_name="Spring",
        # )
        # cls.year = Year.objects.create(
        #     year="2023",
        # )

        # def test_period_model(self):
        #     self.assertEqual(self.period.period_sequence, "1")
        #     self.assertEqual(self.period.period_name, "2023")
        #
        # def test_year_model(self):
        #     self.assertEqual(self.year.year, "2023")
