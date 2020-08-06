from django.shortcuts import render,HttpResponse, redirect

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