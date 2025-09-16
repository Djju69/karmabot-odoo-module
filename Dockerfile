﻿FROM odoo:17.0

# Копировать модуль
COPY addons/ /mnt/extra-addons/

# Создать конфигурационный файл
RUN echo '[options]' > /etc/odoo/odoo.conf && \
    echo 'addons_path = /usr/lib/python3/dist-packages/odoo/addons,/var/lib/odoo/addons/17.0,/mnt/extra-addons' >> /etc/odoo/odoo.conf && \
    echo 'data_dir = /var/lib/odoo' >> /etc/odoo/odoo.conf

# Запустить Odoo
CMD ["odoo"]
