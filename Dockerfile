FROM odoo:17.0

# Копировать модуль
COPY addons/ /mnt/extra-addons/

# Проверить что модуль скопировался
RUN ls -la /mnt/extra-addons/ && \
    ls -la /mnt/extra-addons/karmabot_webapp/

# Создать конфигурационный файл
RUN echo '[options]' > /etc/odoo/odoo.conf && \
    echo 'addons_path = /usr/lib/python3/dist-packages/odoo/addons,/var/lib/odoo/addons/17.0,/mnt/extra-addons' >> /etc/odoo/odoo.conf && \
    echo 'data_dir = /var/lib/odoo' >> /etc/odoo/odoo.conf && \
    echo 'db_host = ${PGHOST:-postgres-dqhn.railway.internal}' >> /etc/odoo/odoo.conf && \
    echo 'db_port = ${PGPORT:-5432}' >> /etc/odoo/odoo.conf && \
    echo 'db_user = ${PGUSER:-odoo}' >> /etc/odoo/odoo.conf && \
    echo 'db_password = ${PGPASSWORD}' >> /etc/odoo/odoo.conf && \
    echo 'db_name = ${PGDATABASE:-railway}' >> /etc/odoo/odoo.conf

# Запустить Odoo
CMD ["odoo"]
