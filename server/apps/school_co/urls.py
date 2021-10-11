from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register(r'school', views.SchoolViewSet, 'school')
router.register(r'pupil', views.PupilViewSet, 'pupil')
router.register(r'learner_text_genre', views.LearnerTextGenreViewSet, 'learnertextgenre')
router.register(r'learner_text', views.LearnerTextViewSet, 'learnertext')
router.register(r'annotation_type', views.AnnotationTypeViewSet, 'annotationtype')
router.register(r'learner_text_annotation', views.LearnerTextAnnotationViewSet, 'learnertextannotation')

urlpatterns = [
    path('api/', include(router.urls)),
]
