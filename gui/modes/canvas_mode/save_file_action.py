from gui.modes.action_base import ActionBase

class SaveFileAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Save File", 
                            icon_filename = "button-save.ico",
                            *args,
                            **kwargs)