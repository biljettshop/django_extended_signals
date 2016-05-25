from extended_signals.signals import form_pre_init, form_post_init, form_clean, form_pre_save, form_post_save


class FormSignalsMixin(object):
    def __init__(self, *args, **kwargs):
        form_pre_init.send(sender=self.__class__, instance=self, args=args, kwargs=kwargs)
        super().__init__(*args, **kwargs)
        form_post_init.send(sender=self.__class__, instance=self, args=args, kwargs=kwargs)

    def clean(self):
        super().clean()
        form_clean.send(sender=self.__class__, instance=self)
        return getattr(self, 'cleaned_data', {})

    def save(self, *args, **kwargs):
        form_pre_save.send(sender=self.__class__, instance=self, args=args, kwargs=kwargs)
        super().save(*args, **kwargs)
        form_post_save.send(sender=self.__class__, instance=self, args=args, kwargs=kwargs)