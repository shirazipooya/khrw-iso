import base64
from dash_bootstrap_components._components.Label import Label
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table

import numpy as np
from datetime import date


from layouts.visualization import *


"""
-------------------------------------------------------------------------------
Tab 1
-------------------------------------------------------------------------------
"""


"""
---------------------------------------
Card 1: 
---------------------------------------
"""

CARD_1_IMG = base64.b64encode(open('assets/images/excel_logo.png', 'rb').read())

CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                html.Img(src='data:image/png;base64,{}'.format(CARD_1_IMG.decode()), height=30),
                "       Load Data From File"
            ],
            className='card-header in'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To An Existing Spreadsheet"
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-success mt-3"
                                ),
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        dcc.Upload([
                            'Drag and Drop or ',
                            html.A(html.B('Select a File')),
                        ],
                            className="upload-button",
                            id="upload_button_TAB1_SIDEBAR_CARD1",
                            accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    ],
                    className='card-text text-center'
                ),
                html.Div(
                    children=[
                        html.Button(
                            children=[
                                "Connect"
                            ],
                            n_clicks=0,
                            className="btn btn-success mt-3",
                            id="connect_button_TAB1_SIDEBAR_CARD1_CONNECT2"
                        ),
                        dbc.Toast(
                            id="database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2",
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            style={
                                "position": "fixed",
                                "top": 48,
                                "right": 50,
                                "width": 350
                            },                        
                        )
                    ],
                    className="d-flex justify-content-end"
                )
            ],
            className='card-body text-dark'
        ),
        html.Div(
            children=[
                html.H6(
                    id="show_filename_selected_TAB1_SIDEBAR_CARD1"
                )
            ],
            className='card-footer'
        ),
    ],
    className='card border-dark mb-2'
)


"""
---------------------------------------
Card 2: 
---------------------------------------
"""

CARD_2_IMG = base64.b64encode(open('assets/images/database_logo.png', 'rb').read())

CARD_2 = html.Div(
    children=[
        html.H6(
            children=[
                html.Img(src='data:image/png;base64,{}'.format(CARD_2_IMG.decode()), height=30),
                "       Load Data From Database"
            ],
            className='card-header in'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To An Existing Database"
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To Database Server"
                            ]
                        ),
                        dcc.Input(
                            placeholder='127.0.0.1:8080',
                            type='text',
                            value='',
                            className="form-control"
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To Local Database"
                            ]
                        ),
                        html.Div(
                            children=[
                                dcc.Upload([
                                    'Drag and Drop or ',
                                    html.A(html.B('Select a File'))
                                ],
                                    className="upload-button")
                            ],
                            className='card-text text-center'
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
            ],
            className='card-body text-dark'
        ),
        html.Div(
            children=[
                "Card Footer"
            ],
            className='card-footer'
        ),
    ],
    className='card border-dark mb-2'
)


"""
---------------------------------------
Sidebar Tab 1
---------------------------------------
"""

SIDEBAR_TAB_1 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        CARD_1,
                        # CARD_2
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)







sidebarTab1 = [
    html.H3(
        className='headerText',
        children=['???????????????? ???????? ?????? ??????????']
    ),
    html.Hr(),
    dbc.Form(
        className='formSidebar',
        children=[
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ???????? ?????? ???????? ????????:'
                        ]
                    ),
                    dbc.Row(
                        align='baseline',
                        children=[
                            dcc.Upload(
                                id='uploadButton_rawData',
                                className='uploadButton',
                                children=[
                                    html.Button('???????????? ????????')
                                ],
                            ),
                            dbc.FormText(
                                id='uploadButtonInfo_rawData',
                                className='uploadButtonInfo'
                            )
                        ]
                    )
                ]
            ),
            html.Br(),
            dbc.Card(
                className='card_sidebar_tab1',
                children=[
                    dbc.CardHeader("?????????????? ???????? ?????? ??????????"),
                    dbc.CardBody(
                        [
                            html.H5("?????????? ???????????? ?????? ??????????",
                                    className="card-title"),
                            html.P(
                                id='number_aquifer_sidebar_tab1',
                                className="card-text",
                            ),
                        ]
                    ),
                    html.Hr(),
                    dbc.CardBody(
                        [
                            html.H5("?????????? ?????? ?????? ???????????? ???? ??????????",
                                    className="card-title"),
                            html.P(
                                id='number_well_sidebar_tab1',
                                className="card-text",
                            ),
                        ]
                    ),
                    html.Br(),
                ],
                color="primary",
                outline=True
            ),
            # Hidden div inside the app that stores info and raw data
            html.Div(
                id='infoData',
                style={
                    'display': 'none'
                }
            ),
            html.Div(
                id='rawData',
                style={
                    'display': 'none'
                }
            ),
            html.Div(
                id='finalData',
                style={
                    'display': 'none'
                }
            ),
        ]
    )
]


sidebarTab2 = [
    html.H3(
        className='headerText',
        children=['?????????????? ??????????']
    ),
    html.Hr(),
    dbc.Form(
        className='formSidebar',
        children=[
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ????????????:'
                        ]
                    ),
                    dcc.Dropdown(
                        id='aquifer_select_sidebar_tab2',
                        placeholder="???? ???????????? ???????????? ????????",
                        className='dropdown'
                    ),
                ]
            ),
            html.Br(),
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ?????? ???????????? ????:'
                        ]
                    ),
                    dcc.Dropdown(
                        id='well_select_sidebar_tab2',
                        placeholder="???? ???? ?????? ?????? ???????????? ???? ???? ???????????? ????????",
                        multi=True,
                        className='dropdown'
                    ),
                ]
            ),

            html.Br(),
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ???????? ??????????:'
                        ]
                    ),

                    html.Div(
                        children=[
                            html.Small(
                                children=[
                                    '?????? ????????'
                                ],
                                style={'width': '30%'}
                            ),
                            dcc.Dropdown(
                                id='start_year_select_tab2',
                                options=[
                                    {'label': '{}'.format(i), 'value': i} for i in range(1381, 1400)
                                ],
                                value=1381,
                                searchable=True,
                                clearable=False,
                                placeholder="????????",
                                className='dropdown',
                                style={'width': '50%'}
                            ),
                        ],
                        className='row',
                        style={
                            'margin-right': '15px'
                        }
                    ),

                    html.Div(
                        children=[
                            html.Small(
                                children=[
                                    '?????? ??????????'
                                ],
                                style={'width': '30%'}

                            ),
                            dcc.Dropdown(
                                id='end_year_select_tab2',
                                options=[

                                ],
                                value=1399,
                                searchable=True,
                                clearable=False,
                                placeholder="??????????",
                                className='dropdown',
                                style={'width': '50%'}
                            ),
                        ],
                        className='row',
                        style={
                            'margin-right': '15px'
                        }
                    ),
                ]
            ),
            html.Br(),
            dbc.FormGroup(
                children=[
                    html.Div(
                        className='div_switch',
                        children=[
                            daq.BooleanSwitch(
                                id='boolean_switch_sidebar_tab2',
                                on=False,
                                color="#9B51E0",
                                label='???????? ???????? ?????? ???? ?????? ???????????? ????',
                                labelPosition="top",
                                disabled=False
                            )
                        ]
                    )
                ]
            ),
            html.Br(),
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    html.Div(
                        children=mapSidebarTab2
                    )
                ]
            ),
        ]
    )
]


sidebarTab3 = [
    html.H3(
        className='headerText',
        children=['?????????????? ??????????']
    ),
    html.Hr(),
    dbc.Form(
        className='formSidebar',
        children=[
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ????????????:'
                        ]
                    ),
                    dcc.Dropdown(
                        id='aquifer_select_sidebar_tab3',
                        placeholder="???? ???????????? ???????????? ????????",
                        multi=True,
                        className='dropdown'
                    ),
                ]
            ),
            dbc.FormGroup(
                className='formgroupSidebar',
                children=mapSidebarTab3
            ),
            html.Br(),
            dbc.FormGroup(
                className='formgroupSidebar',
                children=[
                    dbc.Label(
                        children=[
                            '???????????? ???? ???????? ???????????? ???????????? ?????? ??????????????:'
                        ]
                    ),
                    html.Div(
                        className='div_show_delta_select',
                        children=[
                            dbc.Label(
                                className='show_delta_select',
                                id='show_delta_select_sidebar_tab3'
                            )
                        ]
                    ),
                    dcc.Slider(
                        className='sider_sidebar_tab3',
                        id="delta_select_sidebar_tab3",
                        min=0,
                        max=5,
                        step=0.1,
                        value=0.5,
                        marks={i: str(i)
                               for i in np.arange(0, 5.1, 0.5).tolist()}
                    ),
                    html.Br(),
                    html.Div(
                        className='ss',
                        children=[
                            dcc.Checklist(
                                id='select_mean_aquifer_head',
                                options=[
                                    {'label': '   ?????????????? ??????????',
                                        'value': 'Arithmetic'},
                                    {'label': '   ?????????????? ??????????',
                                        'value': 'Geometric'},
                                    {'label': '   ?????????????? ????????????????',
                                        'value': 'Harmonic'}
                                ],
                                value=['Arithmetic', 'Geometric', 'Harmonic'],
                                labelStyle={'display': 'block'}
                            )
                        ]
                    ),
                    html.Br(),
                    html.Div(
                        className='calculate_button_div',
                        children=[
                            dbc.Button("????????????",
                                       id='calculate_button_sidebar_tab3',
                                       className='calculate_button',
                                       outline=True,
                                       color="secondary",
                                       n_clicks=0)
                        ]
                    )
                ]
            )
        ]
    )
]
