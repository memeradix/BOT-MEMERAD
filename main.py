import requests
import time
import telegram

# Configurações
API_URL = "https://api.ociswap.com/tokens/resource_rdx1t5u04cs3u2yxqkcwku7jdvdvv9cu739jsx0rdwu97682lr0rn92qdh"
TELEGRAM_TOKEN = "7066555286:AAH5yIkl1UaFwIgdnlcnMEO5iiC0Tu31mt0"
CHAT_ID = "-1002577329670"

# Criação do bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Lista de imagens
imagens = [
    "https://media.giphy.com/media/vtlW1FUy2kuserMCvq/giphy.gif",
    "https://media.giphy.com/media/3CiK1J8XREvgVfaGPX/giphy.gif",
    "https://media.giphy.com/media/RJX5hC01asHtIQTMAC/giphy.gif",
    "https://media.giphy.com/media/RJX5hC01asHtIQTMAC/giphy.gif",
    "https://media.giphy.com/media/YZx1BxFIXfMkaNEjVE/giphy.gif",
    "https://media.giphy.com/media/ino7NMUZ9cdXqBjvRM/giphy.gif"
]

ultima_compra_id = None
contador_imagem = 0

def verificar_novas_compras():
    global ultima_compra_id, contador_imagem
    response = requests.get(API_URL)
    
    if response.status_code != 200:
        print("Erro ao acessar a API.")
        return

    data = response.json()

    # Ajuste conforme a estrutura real da API
    # Exemplo simulado:
    compra = {
        'id': data.get('id'),  # precisa ter um identificador único
        'usd': data.get('usdSpent', 0),
        'xrd': data.get('xrdSpent', 0),
        'MRD': data.get('mrdReceived', 0),
        'price': data.get('price', 0),
        'market_cap': data.get('marketCap', 0),
        'holders': data.get('holders', 0)
    }

    if not compra['id']:
        print("Dados de compra incompletos.")
        return

    if compra['id'] != ultima_compra_id:
        ultima_compra_id = compra['id']
        mensagem = f"""🐙 *MEMERAD Buy!*
🐙🐙

➡️ *Spent (TX)*:
${compra['usd']} ({compra['xrd']} XRD)
🔄 *Got*:
{compra['MRD']} MRD
💵 *Price*:
${compra['price']}
💰 *Market Cap*:
${compra['market_cap']}
👥 *Holders*: {compra['holders']}

[Trending](https://ocsiswap.com) | [Chart](https://ocsiswap.com) | [Buy](https://ocsiswap.com/resource_rdx1t5u04cs3u2yxqkcwku7jdvdvv9cu739jsx0rdwu97682lr0rn92qdh)
"""
        bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode=telegram.ParseMode.MARKDOWN)
        bot.send_photo(chat_id=CHAT_ID, photo=imagens[contador_imagem])
        contador_imagem = (contador_imagem + 1) % len(imagens)

# Looping
while True:
    try:
        verificar_novas_compras()
    except Exception as e:
        print("Erro:", e)
    time.sleep(10)
