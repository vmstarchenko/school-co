from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views, parsers, permissions, serializers
from rest_framework.response import Response
from school_co.serializers import SchoolSerializer, PupilSerializer, LearnerTextGenreSerializer, LearnerTextSerializer, AnnotationTypeSerializer, LearnerTextAnnotationSerializer
from school_co.models import School, Pupil, LearnerTextGenre, LearnerText, AnnotationType, LearnerTextAnnotation, LearnerTextScanPage
from drf_spectacular.utils import extend_schema, OpenApiParameter


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer



class LearnerTextGenreViewSet(viewsets.ModelViewSet):
    queryset = LearnerTextGenre.objects.all()
    serializer_class = LearnerTextGenreSerializer



class LearnerTextViewSet(viewsets.ModelViewSet):
    queryset = LearnerText.objects.all()
    serializer_class = LearnerTextSerializer



class AnnotationTypeViewSet(viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer



class LearnerTextAnnotationViewSet(viewsets.ModelViewSet):
    queryset = LearnerTextAnnotation.objects.all()
    serializer_class = LearnerTextAnnotationSerializer



class FileUploadView(views.APIView):
    parser_classes = (parsers.MultiPartParser, )
    permission_classes = [permissions.IsAuthenticated]
    KEYS = {
        'learner_text.scan_page': LearnerTextScanPage,
    }

    class UploadFileSerializer(serializers.Serializer):
        file = serializers.FileField()

    class UploadedFileSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        url = serializers.CharField()
        name = serializers.CharField()
        uid = serializers.CharField()

    @extend_schema(
        operation_id='file_upload',
        parameters=[
            OpenApiParameter('key', str, enum=KEYS.keys(), required=True),
        ],
        request=UploadFileSerializer(),
        responses=UploadedFileSerializer(),
    )
    def post(self, request):
        Model = self.KEYS[request.GET.get('key')]
        uploaded = request.FILES['file']

        obj = Model(user=request.user)
        obj.file.save('name', uploaded)
        print('x', obj.file.path)

        url = request.build_absolute_uri(obj.file.url)

        return Response(self.UploadedFileSerializer({
            'id': obj.id,
            'url': url,
            'name': os.path.basename(obj.file.url),
            'uid': url,
        }).data)
