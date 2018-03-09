# echo "${CRON_TASK}" > /etc/cron.d/crontabfile
# cat /etc/cron.d/crontabfile >> /var/spool/cron/crontabs/root
echo "${CRON_TASK}" >> /var/spool/cron/crontabs/root
crond
touch /var/log/cron.log
tail -F /var/log/cron.log