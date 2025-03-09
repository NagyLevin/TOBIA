from utils.logging import create_sys_logger
logger = create_sys_logger(use_stdout=True)

import asyncio
from utils.server import start_web_server

import os
import importlib

if __name__=="__main__":
    """
    plugin_path = "C:\\Users\\levis\\PycharmProjects\\TOBIA\\plugins\\stt_openai_whisper_lcc"
    print("Folder exists:", os.path.exists(plugin_path))

    init_file = os.path.join(plugin_path, "__init__.py")
    print("Init file exists:", os.path.exists(init_file))

    # List all files inside the folder
    print("\n🔍 Contents of plugin folder:")
    print(os.listdir(plugin_path))

    import sys

    sys.path.insert(0, "C:\\Users\\levis\\PycharmProjects\\TOBIA\\plugins")
    print("\n✅ Plugins directory added to sys.path:", sys.path[0])

    import sys

    print("\n🔍 sys.path Directories:")
    for path in sys.path:
        print(path)

    import pkgutil

    modules = [module.name for module in pkgutil.iter_modules()]
    print("\n🔍 Available Modules:\n", modules)

    try:
        module = importlib.import_module("stt_openai_whisper_lcc")
        print("✅ Successfully imported:", module)
    except ModuleNotFoundError as e:
        print("❌ Import failed:", e)
    
    """
    asyncio.run(start_web_server())

    #TODO install plugins so that the project can run