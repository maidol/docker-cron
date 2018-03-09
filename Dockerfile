FROM alpine:latest
# Install base packages, set timezone
RUN apk update && apk add bash tzdata python
ENV TZ Asia/Shanghai

# ADD crontabfile /etc/cron.d/
ADD tasks /app/tasks
ADD run.sh /

# RUN cat /etc/cron.d/crontabfile >> /var/spool/cron/crontabs/root
#将run.sh设置为可执行
RUN chmod +x /run.sh

CMD ["bash", "/run.sh"]
