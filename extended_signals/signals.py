from django.dispatch.dispatcher import Signal

form_pre_init = Signal()
form_post_init = Signal()
form_pre_save = Signal()
form_post_save = Signal()
form_clean = Signal()

#form_validate = Signal()

#form_initial_data = Signal()

