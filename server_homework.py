#
# Серверное приложение для соединений
#
# Я второй день "программист", постарался оставить комменты там, где накодил
import asyncio
from asyncio import transports


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.buffer = server.buffer

    def data_received(self, data: bytes):
        print(data)

        decoded = data.decode()

        if self.login is not None:
            self.send_message(decoded)

        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")

                if self.login in self.buffer:
                    self.transport.write("Логин занят\n".encode())
                    self.transport.close()  #единственный способ, который я нашел для кика юзера с сервера =\
                else:
                    self.buffer.append(self.login)
                    self.transport.write(f"Привет, {self.login}!\n Список пользователей online: {self.buffer}".encode())

            else:
                self.transport.write("Неправильный логин\n".encode())

    def send_history(self):    #Понимает только латиницу! что то с кодировками наверняка
        self.transport.write(f"{self.server.history}".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")
        self.transport.write("Введите уникальный логин\n".encode())
        self.send_history()   #высылает список из 10 сообщений, разделенных пробелами в кавычках(не знаю, как победить кавычки иначе)

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}: {content}\n"
        self.server.history.append(f"{content}".replace("\r\n", "").strip())
        while len(self.server.history) >= 21:     #21 для вывода пробела между сообщениями
            del self.server.history[0]            #удаляет самые старые сообщения из истории

        for user in self.server.clients:
            user.transport.write(message.encode())


class Server:
    clients: list
    buffer: list       #буфер для хранения логинов пользователей
    history: list       #буфер хранения истории сообщений

    def __init__(self):
        self.clients = []
        self.buffer = []
        self.history = ["Добрый день"]

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
