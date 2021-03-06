import os
from dataclasses import dataclass

bot_token = os.getenv("AUTOHATERBOT_TELEGRAM_TOKEN")
destruction_timeout = int(os.getenv("AUTOHATERBOT_DELETE_TIMEOUT", 180))
whitelist_chats = os.getenv("AUTOHATERBOT_ALLOWED_CHATS", "")

days_without = "Днів без згадування {name}: `0` {emoji}"
bot_start_text = (
    "Привіт, я Рудекіт!\n\n"
    "Я можу дещо зробити, якшо ти скажеш чарівне слово:\n"
    "`Тесла` - порахую дні без згадування тесли,\n"
    "А ще я вітаю новеньких у чаті."
)
new_member_greeting = (
    "Вітаємо {user} у нашому авточаті! "
    "Ми - дружня спільнота, яка поважає думку кожного. "
    "Приєднавшись, ти згоджуєшся стати чемною частиною спільноти."
)
new_member_button_text = "Я обіцяю!"
new_user_warning = "Ще раз і бан :)"
new_user_greeting = (
    "Дуже раді вас бачити! "
    "Будь ласка, ознайомтеся з Конституцією чату в закріплених повідомленнях."
)


@dataclass
class CarMention:
    regexp: str
    name_cyrillic: str
    emoji: str


Skoda = CarMention("[Ss]kod|[Шш]код", "Шкоди", "🚘🚘🚘")
Vag = CarMention("vag|ваг", "ВАГа", "🚙🚙🚙")
Tesla = CarMention("tesl|тесл", "Тесли", "🚗🚗🚗")
