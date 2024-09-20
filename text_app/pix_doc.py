from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static, Input
from textual.screen import Screen

class AuthScreen(Screen):
    """Экран для ввода логина и пароля."""

    def compose(self) -> ComposeResult:
        """Создание виджетов экрана авторизации."""
        yield Static("Login", id="auth-label")
        self.username_input = Input(placeholder="Enter your username", id="username")
        self.password_input = Input(placeholder="Enter your password", id="password")
        yield self.username_input
        yield self.password_input
        yield Button("Submit", id="submit_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Обработчик нажатия на кнопку."""
        if event.button.id == "submit_button":
            self.app.push_screen(MainScreen())

class ContainerRow(Container):
    def __init__(self, name_container: str, state_container: str, image_container: str, **kwargs):
        super().__init__(**kwargs)
        self.name_container = name_container
        self.state_container = state_container
        self.image_container = image_container

    def compose(self) -> ComposeResult:
        """Создание строки для контейнера."""
        yield Static(self.name_container, id="container-name")
        yield Static(self.state_container, id="container-state")
        yield Static(self.image_container, id="container-image")
        yield Button("Start", id="start-btn", variant="success")
        yield Button("Stop", id="stop-btn", variant="error")

class MainScreen(Screen):
    """Следующий экран после авторизации."""

    def compose(self) -> ComposeResult:
        """Создание макета пользовательского интерфейса."""
        # Поисковая строка
        yield Input(placeholder="Search containers...")

        # Заголовки таблицы
        yield Static("Name", id="header-name")
        yield Static("State", id="header-state")
        yield Static("Image", id="header-image")

        # Пример строки для контейнера
        yield ContainerRow(name_container="ams-ai-api_service-1", state_container="exited", image_container="ams-ai-api_service")
        yield ContainerRow(name_container="ams-ai-postgres-1", state_container="running", image_container="postgres:latest")

        # Кнопки управления
        yield Container(
            Button("Start", variant="primary"),
            Button("Stop", variant="error"),
            Button("Restart", variant="warning"),
            Button("Kill", variant="error")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Обработчик нажатия на кнопку."""
        if event.button.id == "back_button":
            self.app.pop_screen()

class MyApp(App):

    def on_mount(self) -> None:
        """Когда приложение запустится, показать первый экран."""
        self.push_screen(AuthScreen())

if __name__ == "__main__":
    app = MyApp()
    app.run()
