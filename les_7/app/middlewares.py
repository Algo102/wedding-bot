# Промежуточное программное обеспечение
# auter - внешний, inner - внутренний
# внешний выполняется до фильтров-хендлеров
# внутренний выполняется после того как диспетчер выбрал нужный хендлер


from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable


class TestMiddleware(BaseMiddleware):  # Дочерний класс от BaseMiddleware
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print('Действия до обработчика')
        result = await handler(event, data)
        print('Действия после обработчика')
        return result

# handler - обработчик, запускается в любой момент и работает ТОЛЬКО для
# внутреннего мидлваре, т.к. внешний еще не знает, какой будет хендлер
# event - тип объекта. TelegramObject - любой объект, но можно указать конкретно Mesage или Callbackdata
# data - доп информация, например FSM
