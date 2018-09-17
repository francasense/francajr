from django.shortcuts import render,redirect
from django.core.mail import EmailMultiAlternatives
import requests, json


siteurl = "http://ninos.pythonanywhere.com/account"

title = 'Ninos App'
# Create your views here.
def home(request):
    subtitle = ['home','pagina inicial Ninos App']
    user = request.user
    if str(user)=="AnonymousUser":
        return render(request,'index.html',dict(title=title,subtitle = subtitle,view="home.html"))
    else:
        return render(request,'index.html',dict(title=title,subtitle = ["home","bem vindo de volta {}".format(user)],view="home.html"))


def confirm(request):
    subs = [['Login','cadastramento de usuário'],['OK','tudo certo!'],['ERRO','ha algo de arrado']]
    erro = None
    #url="https://fsfwefdefeeddfcef.herokuapp.com/register"

    if request.method=="POST":

        #pegou o email do user
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        #senha = request.POST.get('senha')

        url = "https://fsfwefdefeeddfcef.herokuapp.com/registertemp"#OKAY
        payload = {
        "username":nome,
        "password":senha,
        "tipo":"usuario_comum",
        "email":email,
        "telefone":telefone,
        "cpf":cpf,
        "msg":"ok",
        "promocao":"promocao"
        }
        headers = {
        #'content-type': "application/json",
        #"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzYyMDM1MjcsIm5iZiI6MTUzNjIwMzUyNywianRpIjoiZDAwMWY2NzUtMzFmZC00MjcyLThlMzMtMTZjZTQxYzg5NTRiIiwiZXhwIjoxNTM2MjA0NDI3LCJpZGVudGl0eSI6InN1cmFoQGZpZGVsaXVtMTAuY29tIiwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.6XDyCHShiH440HS1FV-_jL101xoK0aIavPOjuFunAR4",
        #charset=utf-8
        #"charset": "utf-8"
        }
        resp = requests.post(url, data=payload, headers=headers)#OKAY

        dicionario = json.loads(resp.text)#OKAY
        status = dicionario['st']
        if status == '1':
            access = dicionario['access_token']
            usuario = dicionario['st']
            id_user = dicionario['st']

            turl = siteurl+"confirm?"+tk.text
            htmlEmail =  """<h3>Termine seu cadastro na NinosApp </h3>
            <p>Para terminar seu cadrastro, <a href="{turl}">click aqui</a><p><br/>
            <p><font color="#f00">obs: </font> você tem apenas 10 minutos para realizar seu cadastro, caso nao seja confirmado, acesse {url} e faça esta etapa novamente
            </p><br/>
            <small>Esta é uma menssagem enviada altomaticamente. Por favor não responsa.</small>""".format(url=siteurl,turl=turl)
            sub = "termine seu cadastro na NinosApp"
            text_content = ''
            f ='suport@ninosapp.com'

            try:
                msg = EmailMultiAlternatives(sub,text_content,f, [email])
                msg.attach_alternative(htmlEmail, 'text/html')
                msg.send()
            except:
                erro = 'email invalido!'
                return render(request,'index.html',dict(view='login.html',title=title,subtitle=subs[0],mode="1",erro = erro))

            return render(request,'index.html',dict(view='next.html',title=title,subtitle=subs[1],form={"usuario":usuario}))

        else:
            return redirect('home')

#coloquei nesse metodo so pra nao criar outro agora é so pra testar o retorno e o cadastro no server blz
def account(request):
    userId = request.GET.get('id')
    token = request.GET.get('tk')

    url = "https://fsfwefdefeeddfcef.herokuapp.com/operacao/"+userId#OKAY
    payload = {
    }
    headers = {
    #aqui tem que passar o token blz ele dura ums 10 min
    'content-type': "application/json",
    "Authorization":"Bearer"+" "+token
    }
    resp = requests.post(url, data=payload, headers=headers)#OKAY

    dicionario = json.loads(resp.text)#OKAY
    username = dicionario['st']
    subtitle = ['conta','Cadastro Confirmado']

    return render(request,'index.html',dict(view='account.html', usuario=username))



def login(request):
    mode = request.GET.get('mode')
    if not mode==None:
        return render(request,'index.html',dict(view='login.html',title=title,mode=mode))
    else:
        return render(request,'index.html',dict(view='login.html',title=title,mode='1'))

def logout(request):
    return render(request,'index.html',dict(view='login.html',title=title))


def api(request):
    subs = [['Login','cadastramento de usuário'],['OK','tudo certo!'],['ERRO','ha algo de arrado']]
    erro = None
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    telefone = request.GET.get('telefone')
    cpf = request.GET.get('cpf')
    senha = request.GET.get('senha')

    url = "https://fsfwefdefeeddfcef.herokuapp.com/registertemp"#OKAY
    payload = {
    "username":nome,
    "password":senha,
    "tipo":"usuario_comum",
    "email":email,
    "telefone":telefone,
    "cpf":cpf,
    "msg":"ok",
    "promocao":"promocao"
    }
    headers = {
    #'content-type': "application/json",
    #"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzYyMDM1MjcsIm5iZiI6MTUzNjIwMzUyNywianRpIjoiZDAwMWY2NzUtMzFmZC00MjcyLThlMzMtMTZjZTQxYzg5NTRiIiwiZXhwIjoxNTM2MjA0NDI3LCJpZGVudGl0eSI6InN1cmFoQGZpZGVsaXVtMTAuY29tIiwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.6XDyCHShiH440HS1FV-_jL101xoK0aIavPOjuFunAR4",
    #charset=utf-8
    #"charset": "utf-8"
    }
    resp = requests.post(url, data=payload, headers=headers)#OKAY

    dicionario = json.loads(resp.text)#OKAY
    status = dicionario['st']
    if status == '1':
        access = dicionario['access_token']
        #usuario = dicionario['st']
        id_user = dicionario['st']

        turl = siteurl+"confirm?"+access+id_user
        htmlEmail =  """<h3>Termine seu cadastro na NinosApp </h3>
        <p>Para terminar seu cadrastro, <a href="{turl}">click aqui</a><p><br/>
        <p><font color="#f00">obs: </font> você tem apenas 10 minutos para realizar seu cadastro, caso nao seja confirmado, acesse {url} e faça esta etapa novamente
        </p><br/>
        <small>Esta é uma menssagem enviada altomaticamente. Por favor não responsa.</small>""".format(url=siteurl,turl=turl)
        sub = "termine seu cadastro na NinosApp"
        text_content = ''
        f ='suport@ninosapp.com'

        try:
            msg = EmailMultiAlternatives(sub,text_content,f, [email])
            msg.attach_alternative(htmlEmail, 'text/html')
            msg.send()
        except:
            erro = 'email invalido!'
            return render(request,'index.html',dict(view='login.html',title=title,subtitle=subs[0],mode="1",erro = erro))

        return render(request,'index.html',dict(view='next.html',title=title,subtitle=subs[1]))

    else:
        return redirect('home')
