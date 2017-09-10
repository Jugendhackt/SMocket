#!/usr/bin/bash
echo Installiere Pakete
apt install apache2 mysqlserver php7.0 hostapd dnsmsq python-rpi.gpio php-mysql -y


echo Kopiere Konfigurations-Dateien in die Systeme
cp /home/pi/Smocket/configs/000-default.conf /etc/apache2/sites-available/
cp /home/pi/Smocket/configs/dhcpcd.conf /etc/
cp /home/pi/Smocket/configs/dnsmasq.conf /etc/
cp /home/pi/Smocket/configs/hostapd.conf /etc/hostapd
cp /home/pi/Smocket/configs/interfaces /etc/network/

echo www-data zu GPIO
adduser www-data gpio

echo Starte Dienste neu
systemctl restart apache2
systemctl restart networking
systemctl restart dhcpcd
systemctl restart hostapd
systemctl restart dnsmasq

echo Datenbank init
mysql -u root < init.sql
echo Datenbank Tabelle Laden
mysql -u root smocket < startdb.sql
