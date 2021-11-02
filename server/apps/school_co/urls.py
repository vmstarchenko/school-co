from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register(r'school', views.SchoolViewSet, 'school')
router.register(r'region', views.RegionViewSet, 'region')
router.register(r'teacher', views.TeacherViewSet, 'teacher')
router.register(r'pupil', views.PupilViewSet, 'pupil')
router.register(r'learner_text_genre', views.LearnerTextGenreViewSet, 'learnertextgenre')
router.register(r'scan_text', views.ScanTextViewSet, 'scantext')
router.register(r'print_text', views.PrintTextViewSet, 'printtext')
router.register(r'scan_page', views.ScanPageViewSet, 'scanpage')
router.register(r'annotation_type', views.AnnotationTypeViewSet, 'annotationtype')
router.register(r'print_annotation', views.PrintAnnotationViewSet, 'printannotation')
router.register(r'scan_annotation', views.ScanAnnotationViewSet, 'scanannotation')

urlpatterns = [
    path('api/upload_file/', views.FileUploadView.as_view()),
]
