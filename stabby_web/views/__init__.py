from .authentication_views import login_view, logout_view

from .custom_login_views import custom_login_view

from .dashboard_views import (
    get_country_chart_data,
    get_deployment_type_chart_data,
    get_lock_type_chart_data,
    get_steel_type_chart_data,
    get_usa_new_vintage_chart_data,
    index,
    set_last_purchase_date,
)

from .knife_views import (
    copy_knife,
    get_knife_grid,
    knives,
    knife_create,
    knife_delete,
    knife_detail,
    knife_update,
)
from .sharpener_views import (
    get_sharpener_grid,
    sharpener_create,
    sharpener_delete,
    sharpener_detail,
    sharpener_update,
    sharpeners,
)
from .blade_views import get_blade_grid, blade_create, blade_update, blade_delete
from .library_views import library, library_item_create
from .work_log_views import (
    get_knife_work_log_grid,
    get_sharpener_work_log_grid,
    work_log_create,
    work_log_delete,
    work_log_update,
)
from .photo_views import photo_create, photo_delete, photo_update

__all__ = [
    "copy_knife",
    "custom_login_view",
    "login_view",
    "logout_view",
    "get_knife_grid",
    "index",
    "knives",
    "knife_create",
    "knife_delete",
    "knife_detail",
    "knife_update",
    "library",
    "library_item_create",
    "get_country_chart_data",
    "get_deployment_type_chart_data",
    "get_lock_type_chart_data",
    "get_sharpener_grid",
    "get_steel_type_chart_data",
    "get_usa_new_vintage_chart_data",
    "set_last_purchase_date",
    "sharpener_create",
    "sharpener_delete",
    "sharpener_detail",
    "sharpener_update",
    "sharpeners",
    "get_blade_grid",
    "blade_create",
    "blade_update",
    "blade_delete",
    "get_knife_work_log_grid",
    "get_sharpener_work_log_grid",
    "work_log_create",
    "work_log_delete",
    "work_log_update",
    "photo_create",
    "photo_update",
    "photo_delete",
]
