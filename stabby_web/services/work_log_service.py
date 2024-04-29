from django.shortcuts import get_object_or_404
from ..models import (
    WorkLog,
)


class WorkLogService:

    @classmethod
    def get_work_log_detail(self, work_log_id):
        return get_object_or_404(WorkLog, work_log_id=work_log_id)

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

    @classmethod
    def save_work_log(self, work_log):
        return work_log.save()
