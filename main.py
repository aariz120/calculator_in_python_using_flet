import flet as ft

def main(page: ft.Page):
    page.title="Calculator"
    page.bgcolor = "#2d2d2d"
    page.window.width=350
    page.window.height=470
    page.padding =10
    
    result_text=ft.Text(value="0", size=28, color="white", text_align="right")
    
    display= ft.Container(
        content=result_text,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
        
        )
    
    number_style={
        "height":60,
        "bgcolor":"#37474F",
        "color":"white",
        "expand":1,
    }
    
    operator_style={
        "height":60,
        "bgcolor":"#FF9500",
        "color":"white",
        "expand":1,
    }
    clear_style={
        "height":60,
        "bgcolor":"#FF3B30",
        "color":"white",
        "expand":1,
    }
    equals_style={
        "height":60,
        "bgcolor":"#34C759",
        "color":"white",
        "expand":1,
    }
    button_grid =[
        [
            ("C",clear_style),
            ("%",operator_style),
            ("/",operator_style),
            ("*",operator_style),
        ],
        [
            ("7",number_style),
            ("8",number_style),
            ("9",number_style),
            ("-",operator_style),
        ],
        [
            ("4",number_style),
            ("5",number_style),
            ("6",number_style),
            ("+",operator_style),
        ],
        [
            ("1",number_style),
            ("2",number_style),
            ("3",number_style),
            ("=",equals_style),
        ],
        [
            ("0",{**number_style,"expand": 2}),
            (".",number_style),
            ("$",operator_style),
            
        ]
    ]   
    
    buttons=[]
    for row in button_grid:
        row_controls = []
        for text,style in row:
            btn=ft.ElevatedButton(
                text=text,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0 
                    )
               )
            row_controls.append(btn)
        buttons.append(ft.Row(row_controls, spacing=5))
    
    page.add(
        
        ft.Column(
            [
                display,
                ft.Column(buttons, spacing=5)
                
                
            ],
            spacing=15
            )
    )
    
    
ft.app(target=main)