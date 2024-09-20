from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static, Input
from textual.screen import Screen
from main_screen import MainScreen

class AuthScreen(Screen):
    """Экран для ввода логина и пароля."""

    CSS_PATH = "auth.tcss"

    def compose(self) -> ComposeResult:
        """Создание виджетов экрана авторизации."""
        yield Static(renderable = "Login", id="auth-label")
        self.username_input = Input(placeholder="Enter your username", id="username")
        self.password_input = Input(placeholder="Enter your password", id="password")
        yield Static(renderable = 'Ошибка', id="error")
        yield self.username_input
        yield self.password_input
        yield Button("Submit", id="submit_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Обработчик нажатия на кнопку."""
        if event.button.id == "submit_button":
            if auth(self.username_input, self.password_input):
                self.app.push_screen(MainScreen())
            else:
                self.remove_class("login")
                self.add_class("error")
                


            
def auth(user, password):
    if user == 'admin' and password == 'password':
        return 1
    return 0