FROM odoo:17.0

COPY ./odoo.conf /etc/odoo/
COPY ./entrypoint.sh /entrypoint.sh
COPY ./wait-for-psql.py /wait-for-psql.py

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
