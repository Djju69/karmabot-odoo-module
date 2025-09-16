FROM odoo:17.0

# Копировать модуль
COPY addons/ /mnt/extra-addons/

# Установить модуль
RUN odoo -d postgres -i karmabot_webapp --stop-after-init
