from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Button, Static, Input
from textual.screen import Screen
from main_screen import MainScreen

class AuthScreen(Screen):
    """Экран для ввода логина и пароля."""

    CSS_PATH = "auth.tcss"

    def compose(self) -> ComposeResult:
        """Создание виджетов экрана авторизации."""
        yield Container(
            Static(renderable = "Log in to your account", id="auth-label"),
            Static(renderable = 'Ошибка', id="error"),
            Vertical(
                Input(placeholder="Enter your username", id="username"),
                Input(placeholder="Enter your password", id="password", password=True),
                    Container(
                        Button("Login", id="submit_button", variant="default"),
                        id='button_container',
                    ),
                id='vertical_input'
            ),
                id='auth_container'
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Обработчик нажатия на кнопку."""
        if event.button.id == "submit_button":
            
            username = self.query_one("#username", Input).value
            password = self.query_one("#password", Input).value

            if auth(username, password):
                self.app.push_screen(MainScreen())
            else:
                self.add_class("label")

            
def auth(user, password):
    """Симуляция аутентификации"""
    if user == 'admin' and password == 'password':
        return 1
    return 0