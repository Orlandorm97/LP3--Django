from django.shortcuts import render,HttpResponse, redirect
from miapp.models import Articulo
from django.db.models import Q

# Create your views here.

layout = """

"""


def index(request):
    estudiantes = ['Orlando Ramos', 'Jean Carlos Cruz', 'Oscar Vilca', 'Nathan Silvera', 'Elias Gomez']
    
    return render(request, 'index.html', {
        'titulo' : 'Inicio',
        'mensaje' : 'Proyecto web con Django (Desde el View)',
        'estudiantes':estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'nombre_autor' : 'Jose Orlando Ramos Machuca'
    })

def rango(request):
    a=1
    b=10
    rango=range(a,b)

    return render(request, 'rango.html', {
        'titulo' : 'Rango entre dos números',
        'a': a,
        'b': b,
        'rango': rango
    })
     
def rango2(request,a=0,b=27):
    if a>b:
        return redirect('rango2', a=b, b=a)

    resultado = f"""
        <h2> Numeros de [{a}; {b}] </h2>
        Resultado = <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li>{a}</li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)


def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=6)
        resultado = f"Articulo: <br> ID: {articulo.id} <br> Título: {articulo.titulo} <br> Contenido: {articulo.contenido}"
    
    except:
        resultado: "<h1> Artículo no encontrado. </h1>"

    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza online en la UNTELS"
    articulo.contenido = "Aula Virtual. Google Meet. Portal. Correo institucional"
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Artículo editado <br> NuevoTítulo: {articulo.titulo} <br> NuevoContenido: {articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.all()
    #articulos = Articulo.objects.order_by('-titulo')
    #articulos = Articulo.objects.filter(titulo = "Tendencias Covid con Power BI")
    #articulos = Articulo.objects.filter(titulo__exact = "Hola")
    #articulos = Articulo.objects.filter(id__gte=6) Mayores e iguales que 6
    #articulos = Articulo.objects.filter(id__gt=6) Mayores que 6
    #articulos = Articulo.objects.filter(id__lt=6) Menores que 6
    #articulos = Articulo.objects.filter(id__lte=6) Menores e iguales que 6
    #articulos = Articulo.objects.filter(titulo__contains = "Gas").exclude(publicado=False)
    #articulos = Articulo.objects.raw("""select * from miapp_articulo where id>=6"""    )
    #articulos = Articulo.objects.filter(Q(titulo__contains = "Gas") | Q(titulo__contains= "Covid"))
    

    return render(request,'listar_articulos.html',{
        'articulos': articulos,
        'titulo': 'Listado de Articulos',
    })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()

    return redirect('listar_articulos')

def save_articulo(request):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def create_articulo(request):
    return render(request, 'create_articulo.html')

