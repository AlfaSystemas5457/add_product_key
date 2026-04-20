{
    "name": "Agrega la clave de producto",
    "version": "1.0",
    "description": "Agrega la clade de producto a la interfaz y recibo de punto de venta.",
    "summary": "Agrega la clade de producto a la interfaz y recibo de punto de venta.",
    "author": "DGV",
    # 'website': '',
    "license": "LGPL-3",
    "category": "Point of Sale",
    "depends": ["point_of_sale"],
    # "data": [""],
    "auto_install": False,
    "application": False,
    "assets": {
        "point_of_sale._assets_pos": [
            "add_product_key/static/src/**/*",
        ],
    },
}
