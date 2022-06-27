importar  telebot

 solicitações de importação
de  bs4  importe  BeautifulSoup
da  hora  importar  dormir

CHAVE_API  =  "5447888932:AAEUsJY8gBnvEKNCorIDnYQaFExY4_3PT0I"

bot  =  telebot . TeleBot ( CHAVE_API )

@bot . _ message_handler ( comandos = [ "iniciar_bot" ])
def  opcao1 ( mensagem ):
    
    enquanto  Verdadeiro :
        resposta  =  solicitações . obter ( 'https://kitblaze.com/double/' )

        conteúdo  =  resposta . contente

        site  =  BeautifulSoup ( conteúdo , 'html.parser' )

        noticia  =  site . find ( class_ = 'content-giros' )
        
        atualizado  =  noticia . encontrar ( class_ = 'pdi' )
        
        apóstata  =  atualizado . find ( class_ = 'numero-span' )
        img  =  atualizado . find ( class_ = 'figura-img' )
        
        cor  =  str ( img )

        if  'https://kitblaze.com/wp-content/themes/kitblaze_one/assets/images/black-0.svg'  em  cor :
            defcor  =  "Preto"
            
        elif  "https://kitblaze.com/wp-content/themes/kitblaze_one/assets/images/red-0.svg"  em  cor :
            defcor  =  "Vermelho"

        elif  "https://kitblaze.com/wp-content/themes/kitblaze_one/assets/images/white.svg"  em  cor :
            defcor  =  "Branco"
            
        mais :
            imprima ( "Erro" )

            
        if  defcor  ==  "Branco" :
            texto  =  f"⚪ { defcor } "
            
        elif  defcor  ==  "Vermelho" :
            texto  =  f"🔴   { apóstata . text }  { defcor } "
            
        elif  defcor  ==  "Preto" :
            texto  =  f"   ⚫ { apóstata . texto }  { defcor } "
            
        bot . send_message ( mensagem . chat . id , texto )
            
        dormir ( 30 )

def  controle ( mensagem ):
    retornar  Verdadeiro

@bot . _ message_handler ( func = verificar )
def  respondedor ( mensagem ):
    texto  =  """
Digite /iniciar_bot, ou clique aqui
        ^^^^^^^^^^^
!Responder qualquer outra coisa não vai funcionar."""
    bot . respond_to ( mensagem , texto )

bot . sondagem ()
