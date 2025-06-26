# Используем официальный образ Jenkins LTS с OpenJDK 11 (или 17)
FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Обновляем пакеты и устанавливаем необходимые утилиты
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    curl \
    ca-certificates \
    software-properties-common \
    apt-transport-https \
    nano \
    python3 \
    python3-pip \
    python3-venv \ 
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Добавляем репозиторий Google Chrome и устанавливаем Chrome Stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*
    
# Установка Allure CLI
ENV ALLURE_VERSION 2.27.0
RUN wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip && \
    unzip allure-${ALLURE_VERSION}.zip -d /opt/ && \
    mv /opt/allure-${ALLURE_VERSION} /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm allure-${ALLURE_VERSION}.zip    

# Сделаем python3 и pip доступными как python и pip (по желанию)
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Возвращаемся к пользователю Jenkins
USER jenkins
