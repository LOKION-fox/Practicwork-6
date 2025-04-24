import aiohttp
import asyncio
from datetime import datetime

API_KEY = "EDWnLZwA5MG3ap5wNdAhHA==bZ47XxAyHhAwZ3Mr"
ANIMALS = ["cats", "dogs"]

async def fetch_animal_facts(session, animal_type):
    url = f"https://api.api-ninjas.com/v1/{animal_type}?name=a"
    try:
        async with session.get(url, headers={'X-Api-Key': API_KEY}) as response:
            if response.status == 200:
                data = await response.json()
                return data[:5]  
            print(f"Ошибка {response.status} при запросе {animal_type}: {await response.text()}")
            return None
    except Exception as e:
        print(f"Ошибка соединения: {str(e)}")
        return None

async def main():
    print("=== Информация о различных животных ===")
    start_time = datetime.now()
    
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_animal_facts(session, animal)) for animal in ANIMALS]
        results = await asyncio.gather(*tasks)
        
        for animal_type, animals in zip(ANIMALS, results):
            print(f"\n{animal_type.upper()}:")
            if animals:
                for i, animal in enumerate(animals, 1):
                    print(f"{i}. {animal.get('name', 'Без названия')} - {animal.get('origin', 'Неизвестно')}")
            else:
                print("Данные не получены")
    
    end_time = datetime.now()
    print(f"\nВремя выполнения: {(end_time - start_time).total_seconds():.2f} сек")

if __name__ == "__main__":
    asyncio.run(main())