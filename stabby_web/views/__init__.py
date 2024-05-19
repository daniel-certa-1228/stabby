from .authentication_views import login_view, logout_view
from .knife_views import (
    get_knife_grid,
    index,
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
from .work_log_views import (
    get_knife_work_log_grid,
    get_sharpener_work_log_grid,
    work_log_create,
    work_log_delete,
    work_log_update,
)
from .photo_views import photo_create, photo_update

__all__ = [
    "login_view",
    "logout_view",
    "get_knife_grid",
    "index",
    "knife_create",
    "knife_delete",
    "knife_detail",
    "knife_update",
    "get_sharpener_grid",
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
]
