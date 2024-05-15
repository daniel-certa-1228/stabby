from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import (
    WorkLog,
)


class WorkLogService:

    @classmethod
    def delete_work_log(cls, work_log):
        work_log.is_active = False

        return work_log

    @classmethod
    def get_sharpener_work_log_grid(cls, sharpener):
        queryset = WorkLog.objects.filter(is_active=True, sharpener=sharpener).order_by(
            "-date"
        )

        return list(queryset.values())

    @classmethod
    def get_knife_work_log_grid(cls, knife_id):
        queryset = WorkLog.objects.filter(is_active=True, knife_id=knife_id).order_by(
            "-date"
        )

        return list(queryset.values())

    @classmethod
    def get_work_log_detail(cls, work_log_id):
        return get_object_or_404(WorkLog, work_log_id=work_log_id)

    @classmethod
    def map_work_log_form_to_data(cls, form, knife=None, sharpener=None, work_log=None):
        if work_log == None:
            work_log = WorkLog()
            work_log.create_date = timezone.now()
            work_log.knife = knife
            work_log.sharpener = sharpener

        work_log.edit_date = timezone.now()
        work_log.date = form.cleaned_data["date"]
        work_log.description = form.cleaned_data["description"]

        return work_log

    @classmethod
    def save_work_log(cls, work_log):
        return work_log.save()

    @classmethod
    def show_work_log_card(cls, knife_id=None, sharpener_id=None):
        if knife_id:
            count = WorkLog.objects.filter(is_active=True, knife_id=knife_id).count()

            return count > 0
        elif sharpener_id:
            count = WorkLog.objects.filter(
                is_active=True, sharpener_id=sharpener_id
            ).count()

            return count > 0
        else:
            return False
