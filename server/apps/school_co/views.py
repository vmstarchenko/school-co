from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views, parsers, permissions, serializers
from rest_framework.response import Response

from .forms import RegistrationFormTeacher
from .serializers import SchoolSerializer, PupilSerializer, LearnerTextGenreSerializer, AnnotationTypeSerializer, PrintAnnotationSerializer, ScanAnnotationSerializer, \
    RegionSerializer, TeacherSerializer, ScanTextSerializer, PrintTextSerializer, ScanPageSerializer
from .models import School, Pupil, LearnerTextGenre, AnnotationType, PrintAnnotation, ScanPage, ScanAnnotation, Region, \
    Teacher, ScanText, PrintText
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def registration_teacher_view(request):
    context = {}
    if request.POST:
        form = RegistrationFormTeacher(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password=raw_password)
            login(request, account)
            return redirect('admin')# -----> whereeeeeee??
        else:
            context['teacher_registration_form'] = form
    else:
        form = form = RegistrationFormTeacher()
        context['teacher_registration_form'] = form
    return render (request, 'account/register.html', context) #TODO jwt



class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer


class LearnerTextGenreViewSet(viewsets.ModelViewSet):
    queryset = LearnerTextGenre.objects.all()
    serializer_class = LearnerTextGenreSerializer


class ScanTextViewSet(viewsets.ModelViewSet):
    queryset = ScanText.objects.all()
    serializer_class = ScanTextSerializer


class PrintTextViewSet(viewsets.ModelViewSet):
    queryset = PrintText.objects.all()
    serializer_class = PrintTextSerializer


class ScanPageViewSet(viewsets.ModelViewSet):
    queryset = ScanPage.objects.all()
    serializer_class = ScanPageSerializer


class AnnotationTypeViewSet(viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer


class PrintAnnotationViewSet(viewsets.ModelViewSet):
    queryset = PrintAnnotation.objects.all()
    serializer_class = PrintAnnotationSerializer


class ScanAnnotationViewSet(viewsets.ModelViewSet):
    queryset = ScanAnnotation.objects.all()
    serializer_class = ScanAnnotationSerializer


class FileUploadView(views.APIView):
    parser_classes = (parsers.MultiPartParser, )
    permission_classes = [permissions.IsAuthenticated]
    KEYS = {
        'learner_text.scan_page': ScanPage,
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
