from gui.modes.action_base import ActionBase

class OpenFileAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Open File", 
                            icon_filename = "button-open.ico",
                            *args,
                            **kwargs)