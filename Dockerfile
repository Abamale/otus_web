# Используем официальный образ Jenkins LTS
FROM jenkins/jenkins:lts

# Запускаем от root для установки пакетов
USER root

# Установка Docker Engine и Compose Plugin
RUN apt-get update && \
    apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release && \
    # Создаём папку под ключи
    install -m 0755 -d /etc/apt/keyrings && \
    # Ключ Docker
    curl -fsSL https://download.docker.com/linux/debian/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    # Репозиторий Docker
    echo \
    "deb [arch=$(dpkg --print-architecture) \
    signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    # Устанавливаем Docker и Compose
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
    # Чистим кэш APT
    rm -rf /var/lib/apt/lists/*

# Вернём пользователя Jenkins
USER jenkins