import gradio as gr

# Detect Gradio major version
_GRADIO_VERSION = tuple(int(x) for x in gr.__version__.split('.')[:2])
IS_GRADIO_4 = _GRADIO_VERSION[0] >= 4

def js_kwarg(js_code: str):
    """Return dict with correct key for javascript callback ('js' for 4.x, '_js' for 3.x)."""
    if IS_GRADIO_4:
        return {'js': js_code}
    else:
        return {'_js': js_code}

def safe_info(msg: str):
    """Show info message using gr.Info if available, else print to console."""
    if hasattr(gr, 'Info'):
        gr.Info(msg)
    else:
        print(f"[INFO] {msg}")

def safe_error(msg: str, duration: float = None):
    """Show error message using gr.Error, without 'visible' argument."""
    if hasattr(gr, 'Error'):
        if duration is not None:
            gr.Error(msg, duration=duration)
        else:
            gr.Error(msg)
    else:
        print(f"[ERROR] {msg}")