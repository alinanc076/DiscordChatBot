import discord
from discord.ext import commands 

# Botun prefixi (komutları başlatmak için kullanılacak sembol)
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini almak için izin veriyoruz

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot hazır olduğunda çalışacak olan fonksiyon
@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

# !iklim komutu: İklim değişikliği hakkında genel bilgi verir
@bot.command()
async def iklim(ctx):
    bilgi = (
        "İklim değişikliği, dünya genelindeki hava koşullarının uzun dönemdeki "
        "değişimidir. İnsan faaliyetleri, özellikle fosil yakıtlar ve sera gazları, "
        "gezegenin ortalama sıcaklığını artırmaktadır. Bu durum çevre üzerinde "
        "çarpıcı etkiler yaratmaktadır.\n\n"
        "İklim değişikliğinin başlıca etkileri şunlardır:\n"
        "- Deniz seviyelerinin yükselmesi\n"
        "- Aşırı hava olaylarının (kuraklık, sel, fırtına) artması\n"
        "- Ekosistemlerin bozulması\n"
        "- Tarım alanlarının zarar görmesi\n\n"
        "Herkesin iklim değişikliği ile mücadelede rolü vardır. Bu nedenle, "
        "yenilenebilir enerji kullanmak, doğayı korumak ve çevre dostu alışkanlıklar "
        "geliştirmek büyük önem taşır."
    )
    await ctx.send(bilgi)

# !etkiler komutu: İklim değişikliğinin etkileri hakkında bilgi verir
@bot.command()
async def etkiler(ctx):
    etkiler = (
        "İklim değişikliğinin etkileri şunlardır:\n"
        "- **Deniz Seviyesi Yükselmesi:** Küresel ısınma nedeniyle deniz seviyeleri yükseliyor, bu da "
        "kıyı bölgelerinde sel riski oluşturuyor.\n"
        "- **Kuraklıklar ve Aşırı Sıcaklıklar:** Bazı bölgelerde uzun süreli kuraklıklar ve aşırı sıcaklıklar artıyor.\n"
        "- **Fırtınalar ve Tufanlar:** Havanın daha da aşırı hale gelmesi, güçlü fırtınaların oluşmasına yol açıyor.\n"
        "- **Ekosistem Bozulması:** Sıcaklıklar arttıkça, bitki ve hayvanların yaşam alanları yok olabilir.\n"
        "- **Tarım ve Gıda Güvenliği:** İklim değişikliği tarım ürünlerinin verimliliğini etkileyebilir."
    )
    await ctx.send(etkiler)

# !cozumler komutu: İklim değişikliğine karşı alınacak önlemler hakkında bilgi verir
@bot.command()
async def cozumler(ctx):
    cozumler = (
        "İklim değişikliği ile mücadele için alınabilecek bazı önlemler şunlardır:\n"
        "- **Yenilenebilir Enerji:** Fosil yakıtlar yerine güneş, rüzgar ve hidroelektrik enerji kaynakları kullanılabilir.\n"
        "- **Ağaçlandırma:** Ormanlar, karbon emilimini artırarak iklim değişikliğinin etkilerini hafifletebilir.\n"
        "- **Enerji Verimliliği:** Enerji tüketimini azaltan teknolojilere yatırım yapılabilir.\n"
        "- **Sıfır Atık Hareketi:** Geri dönüşüm, plastik kullanımını azaltma ve atık yönetimi stratejileri uygulanabilir.\n"
        "- **Sıfır Karbon Teknolojileri:** Karbon salınımını sıfıra indirmeyi hedefleyen endüstriyel yenilikler geliştirilmelidir."
    )
    await ctx.send(cozumler)

# Botu çalıştırmak için token girin
bot.run('token')
