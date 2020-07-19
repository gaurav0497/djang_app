from django.shortcuts import HttpResponse



def index(request):
    return HttpResponse("<script>document.location='/shoopeasy'</script>")