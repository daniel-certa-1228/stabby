from .knife_views import get_knife_grid, index, knife_create, knife_detail, knife_update
from .sharpener_views import (
    get_sharpener_grid,
    sharpener_detail,
    sharpeners,
    sharpener_create,
    sharpener_update,
)
from .blade_views import get_blade_grid, blade_create, blade_update
from .work_log_views import (
    get_knife_work_log_grid,
    get_sharpener_work_log_grid,
    work_log_create,
    work_log_update,
)
