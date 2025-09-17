FROM odoo:17.0

# Копировать модуль
COPY addons/ /mnt/extra-addons/

# Проверить что модуль скопировался
RUN ls -la /mnt/extra-addons/ && \
    ls -la /mnt/extra-addons/karmabot_webapp/

# Копировать скрипт запуска
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Запустить Odoo через скрипт
CMD ["/start.sh"]
