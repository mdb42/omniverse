from gui.modes.action_base import ActionBase

class UndoAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(name = "Undo", 
                            icon_filename = "button-undo.ico",
                            *args,
                            **kwargs)
        self.button.setEnabled(False)
        