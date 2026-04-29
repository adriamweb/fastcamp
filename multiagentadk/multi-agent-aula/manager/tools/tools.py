from datetime import datetime

# comentário feito po mim:
# ferramenta que retorna a data e hora atual já formatada, sendo usada quando há necessidade
# de conhecer  a data e hora atual.

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
