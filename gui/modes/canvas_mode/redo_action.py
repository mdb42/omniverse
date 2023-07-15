from gui.modes.action_base import ActionBase

class RedoAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Undo", 
                            icon_filename = "button-redo.ico",
                            *args,
                            **kwargs)
        self.button.setEnabled(False)