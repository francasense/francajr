
#metodo pra cadastrar usuarios pelo celular....
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
    headers = {}
    resp = requests.post(url, data=payload, headers=headers)#OKAY

    dicionario = json.loads(resp.text)#OKAY
    status = dicionario['st']
    if status == '1':
        access = dicionario['access_token']
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
