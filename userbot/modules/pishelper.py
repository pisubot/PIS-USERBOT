""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ghelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Owner](t.me/Apisesad)"
        "\n[Repo](https://github.com/pisubot/Pis-Userbot)"
        "\nTeam [Klick Here](https://t.me/devoloperflicks/32)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/pisubot/Pis-Userbot/Pis-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.ghelp`\
\nUsage: Bantuan Untuk Pis-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
