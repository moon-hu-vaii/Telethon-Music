import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5819029533:AAEStxFY71C8kL3-L_6MPjs_QpXyIP9EREg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHsBu6ZLF4YoyXw2KYWcdkidacoVtxqWPWq4MWGHNJ2ZBfApOATpjAD7k6J2Da08E09iigveNV3KRHbUF5vYi_uEAd2GAL2L-vEge9VdUCPpWgt_7c-_d5E_pUzDXrIu67gGYv0xG0_uUwgNmHicEpvejSNkpOG7TWQpzu6TpsZqnpSFNPws-uqwS-x5blr3854lZzJoeV_YrxmKIMiCvpfwqGLQxelcWA-T4IUb9r2D6ocPDKa2OEMwST_qAz_fe6RqgsjSxi4UNmH8GtThOkZ_9XKKS2FuRR30V1uonDU-Ya3QrzTTTLTii5T8zrmsOqhlHiSmvJH5wujXjY9kK-1h-RA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
