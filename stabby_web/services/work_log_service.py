import datetime
from django.shortcuts import get_object_or_404
from ..models import (
    Knife,
    Sharpener,
    WorkLog,
)


class WorkLogService:

    @classmethod
    def delete_work_log(cls, work_log: WorkLog):
        work_log.is_active = False

        return work_log

    @classmethod
    def get_knife_work_log_grid(cls, knife_id: int):
        queryset = WorkLog.objects.filter(is_active=True, knife_id=knife_id).order_by(
            "-date"
        )

        return list(queryset.values())

    @classmethod
    def get_sharpener_work_log_grid(cls, sharpener_id: int):
        queryset = WorkLog.objects.filter(
            is_active=True, sharpener_id=sharpener_id
        ).order_by("-date")

        return list(queryset.values())

    @classmethod
    def get_work_log_detail(cls, work_log_id: int):
        return get_object_or_404(WorkLog, work_log_id=work_log_id)

    @classmethod
    def map_work_log_form_to_data(
        cls,
        form,
        now: datetime,
        knife: Knife = None,
        sharpener: Sharpener = None,
        work_log: WorkLog = None,
    ):
        if work_log == None:
            work_log = WorkLog()
            work_log.create_date = now
            work_log.knife = knife
            work_log.sharpener = sharpener

        work_log.edit_date = now
        work_log.date = form.cleaned_data["date"]
        work_log.description = form.cleaned_data["description"]

        return work_log

    @classmethod
    def save_work_log(cls, work_log: WorkLog):
        return work_log.save()

    @classmethod
    def show_work_log_card(cls, knife_id: int = None, sharpener_id: int = None):
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
