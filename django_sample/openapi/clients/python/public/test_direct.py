#!/usr/bin/env python3
"""
Прямой тест клиента без относительных импортов
"""

import sys
import os

# Добавляем текущую папку в путь
sys.path.insert(0, os.path.dirname(__file__))

try:
    # Импортируем напрямую
    import api_config
    import services.api_service as api_service
    import models
    
    print("✅ Импорты успешны!")
    
    # Создаем конфигурацию
    config = api_config.APIConfig()
    config.base_path = 'http://localhost:8000'
    config.access_token = 'test-token'
    
    print("🔧 Конфигурация создана:")
    print(f"   - Base URL: {config.base_path}")
    print(f"   - Access Token: {config.access_token}")
    
    # Тестируем получение списка постов
    print("\n🚀 Тестируем API...")
    posts = api_service.api_public_api_posts_list(api_config_override=config)
    
    print("✅ Успешно получен список постов!")
    print(f"📊 Количество постов: {len(posts.results) if posts.results else 0}")
    
    if posts.results:
        print("\n📝 Первый пост:")
        first_post = posts.results[0]
        print(f"   - ID: {first_post.id}")
        print(f"   - Заголовок: {first_post.title}")
        print(f"   - Автор: {first_post.author.username if first_post.author else 'N/A'}")
    
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("💡 Убедитесь, что клиент сгенерирован корректно")
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print("💡 Проверьте, что Django сервер запущен на localhost:8000") 