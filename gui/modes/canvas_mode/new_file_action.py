from gui.modes.action_base import ActionBase

class NewFileAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "New File", 
                            icon_filename = "button-new.ico",
                            *args,
                            **kwargs)