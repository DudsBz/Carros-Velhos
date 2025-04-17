import flet as ft
from database import cars

def main(page: ft.Page):

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    """def clicar(e):
        dlg = ft.AlertDialog(
            title=ft.Text('Cliquei'),
            actions=[
                ft.TextButton('Fechar', on_click=lambda e: page.close(dlg)),
            ],
        )
        page.open(dlg)"""

    page.title = "Carros"
    page.window.width = 400
    page.window.height = 650

    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.DIRECTIONS_CAR_FILLED),
        leading_width = 40,
        title=ft.Text("Carros"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                icon=ft.icons.NOTIFICATIONS,
                icon_color=ft.colors.PURPLE,
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Perfil",
                        icon=ft.icons.PERSON,
                    ),
                    ft.PopupMenuItem(
                        text="Configuração",
                        icon=ft.icons.SETTINGS,
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Mostrar Todos",
                        checked=False,
                        on_click=check_item_clicked,
                    ),
                ],
            ),
        ]

    )

    cars_list = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
        spacing=10,

    )
    for car in cars:
        car_component = ft.ListTile(
            leading=ft.Image(
                src=car['foto'],
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                width=100,
                height=100,
                border_radius=ft.border_radius.all(5),
            ),
            title=ft.Text(f"{car['marca']} - {car['modelo']}"),
        )
        cars_list.controls.append(car_component)

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                label="Usados",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.CAR_RENTAL,
                label="Novos",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.ELECTRIC_CAR,
                label="Elétricos",
            ),
        ],
    )

    page.add(
        app_bar,
        cars_list,
        nav_bar,
        )
    
    


ft.app(main)
