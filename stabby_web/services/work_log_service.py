from ..models import (
    WorkLog,
)


class WorkLogService:

    @classmethod
    def get_sharpener_work_log_grid(self, sharpener):
        queryset = WorkLog.objects.filter(is_active=1, sharpener=sharpener).order_by(
            "-date"
        )

        return list(queryset.values())

    @classmethod
    def get_knife_work_log_grid(self, knife_id):
        queryset = WorkLog.objects.filter(is_active=1, knife_id=knife_id).order_by(
            "-date"
        )

        return list(queryset.values())
