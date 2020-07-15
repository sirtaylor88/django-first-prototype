from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.

class CourseNewView(View):
    template_name = "courses/new.html"
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = { "form": form }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = { "form": form }
        return render(request, self.template_name, context)

class CourseIndexView(View):
    template_name = "courses/index.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)

# class MyIndexView(CourseIndexView):
#     queryset = Course.objects.filter(id=1)

class CourseShowView(View):
    template_name = "courses/show.html"
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)
    # def post(self, request, id=None, *args, **kwargs):
    #     return render(request, self.template_name, {})

class CourseEditView(View):
    template_name = "courses/edit.html"
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context = { "object": obj,
                        "form": form }
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context = { "object": obj,
                        "form": form }
        return render(request, self.template_name, context)

class CourseDeleteView(View):
    template_name = "courses/delete.html"
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context = { "object": obj }
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context = { "object": None }
            return redirect("/courses/")
        return render(request, self.template_name, context)

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, "about.html", {})
