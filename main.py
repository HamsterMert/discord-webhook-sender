from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
import time


print(f'''{Fore.RED}
    ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
    ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
    ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
    ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
    ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                            {Fore.YELLOW}HamsterMert                     ''')
                        
print('   ')
print('   ')

webhookurl = input('Webhook URL nedir? \n > ')

while True:
    
    print(f'''
{Fore.YELLOW}[1]{Style.RESET_ALL} - Mesaj Gönderici
{Fore.YELLOW}[2]{Style.RESET_ALL} - Embed Mesaj Gönderici 
{Fore.YELLOW}[3]{Style.RESET_ALL} - Zamanlı Mesaj Gönderici ve Düzenleyici 
{Fore.MAGENTA}[4]{Style.RESET_ALL} - Everyone Spam (Riskli) 
{Fore.MAGENTA}[5]{Style.RESET_ALL} - Here Spam (Riskli)
{Fore.GREEN}[E]{Style.RESET_ALL} - Webhook Düzenle
{Fore.RED}[Q]{Style.RESET_ALL} - Çıkış''')
    
    secim = input('Seçimi yapınız. \n > ')
    
    if secim == '1':
        webhookmsg = input('Göndermek istediğiniz mesaj nedir? \n > ')
        webhook = DiscordWebhook(url= webhookurl, content= webhookmsg)
        response = webhook.execute()
        print('✔ | Mesaj gönderildi.')

    elif secim == '2':
        webhooktitle = input('Göndermek istediğiniz mesaj nedir? (title) \n > ')     
        webhookdescription = input('Göndermek istediğiniz mesaj nedir? (description) \n > ')
        webhook = DiscordWebhook(url = webhookurl)
        embed = DiscordEmbed(title=webhooktitle, description=webhookdescription, color="ffffff")
        embed.set_footer(text="HamsterMert tarafından | hemstir.now.sh")
        webhook.add_embed(embed)
        response = webhook.execute()
        print('✔ | Mesaj gönderildi.')

    elif secim == '3':

        webhookmsg = input('Gönderilecek mesaj nedir? \n > ')
        webhookedit = input('Düzenlenecek mesaj nedir? \n > ')
        webhooktime = input('Ne zaman sonra mesaj düzenlensin? (saniye cinsinden) \n > ')

        webhook = DiscordWebhook(url=webhookurl, content=webhookmsg)
        webhook.execute()
        print('✔ | Mesaj gönderildi {} saniye sonra mesaj düzenlenecek.'.format(webhooktime))
        webhook.content = webhookedit
        time.sleep(int(webhooktime))
        webhook.edit()
        print('✔ | Mesaj düzenlendi.')

    elif secim == '4':
            webhookcount = int(input('Ne kadar spamlasın? \n > '))
            webhooksended = 0
            while True:
                webhook = DiscordWebhook(url= webhookurl, content='@everyone')
                response = webhook.execute()
                webhooksended = webhooksended + 1
                print('✔ | {} mesaj gönderildi.'.format(webhooksended))
                time.sleep(1)
                if webhookcount == webhooksended:
                    print('✔ | Mesajlar gönderildi.')
                    break

    elif secim == '5':
            webhookcount = int(input('Ne kadar spamlasın? \n > '))
            webhooksended = 0
            while True:
                webhook = DiscordWebhook(url= webhookurl, content='@here')
                response = webhook.execute()
                webhooksended = webhooksended + 1
                print('✔ | {} mesaj gönderildi.'.format(webhooksended))
                time.sleep(1)
                if webhookcount == webhooksended:
                    print('✔ | Mesajlar gönderildi.')
                    break

    elif secim == 'e' or 'E':
        webhookurl = input('Webhook URL nedir? \n > ')

    elif secim == 'q' or 'Q':
        print('Çıkış yapılıyor...')
        time.sleep(3)
        break

    else:
        print('Hatalı seçim yapıldı.')
        