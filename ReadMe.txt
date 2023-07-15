Omniverse

Overview
Omniverse is a dynamic PyQt6 application that presents a robust interface for interacting with OpenAI's language models and other functionalities. The primary user interface consists of three sections:

1. A central display panel for showcasing different interactions based on the current mode.
2. A left panel housing advanced control widgets, also determined by the current mode.
3. A right panel that serves as a chat interface for communication with language models.
The application has a mode selection toolbar at the top left of the window, which allows users to switch between various modes. Each mode can define additional toolbars that appear alongside the mode selection toolbar.

Modes
Omniverse has an abstract ModeBase class that serves as the blueprint for creating new modes. Each mode includes essential information such as its name, description, icon, control UI, and display object. Modes can also define sets of toolbars based on their specific needs.

The application currently has three modes under development:

1. PresentationMode: Presents various simulation spaces for AI agents.
2. CanvasMode: Allows users to interact with DALL-E 2 for image generation, providing multiple toolbars for file actions, setting actions, draw actions, and edit actions.
3. BlueprintMode: Provides a programming interface for dynamic creation and interaction with language learning models.

Actions
All modes have access to an ActionBase class that defines standard actions. These actions consist of names, descriptions, tool tips, icons, and activation handlers.

Directories
* art: Manages the generation and saving of images. This is currently linked to the CanvasMode for painting images onto the scene.
* audio: Manages sound effects and TTS functionality.
* data: Manages all interactions with the local Users SQL database. It provides session management with user API keys encrypted and user passwords hashed.
* llms: Manages interaction with language learning models. It includes callback managers, memory classes for managing the context and groundings, and dynamic chain classes to switch the system prompt template based on the current protocol.

Future Plans
We are continuously improving and adding new features to the application. In the pipeline, we have plans to implement functionalities such as audio recording, speech-to-text integration, user login process, and a persona-focused multi-agent system for managing language learning models.

Note
Users looking to utilize the program currently need to create their own /local/constants.py file with session details. A user-friendly login process is under development and will be integrated soon.









        


        


