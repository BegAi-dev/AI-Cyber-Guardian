import pygetwindow as gw
import google.generativeai as genai
from google.generativeai.types import RequestOptions
import time, os, ctypes, sys

# --- KONFİGÜRASYON ---
API_KEY = "AIzaSyDzOkONgbgjt0vLL721NKfXmsuIG8Fb9nE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def ghost_mode():
    """Pencereyi gizler, X butonu imkansız hale gelir."""
    hWnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hWnd != 0: ctypes.windll.user32.ShowWindow(hWnd, 0)

def ai_karar_ver(baslik):
    """Her şeyi Gemini'a soran ana motor."""
    prompt = f"Sen Jarvis'sin. '{baslik}' başlığı müstehcen mi? En ufak şüphede DANGER yaz. SAFE veya DANGER dışında cevap verme."
    try:
        response = model.generate_content(prompt, request_options=RequestOptions(api_version='v1'))
        return response.text.strip().upper()
    except: return "SAFE"

def baslat():
    ghost_mode() # Tıklar tıklamaz gizlenir!
    son_baslik = ""
    while True:
        try:
            pencere = gw.getActiveWindow()
            if pencere and pencere.title:
                su_anki = pencere.title
                if su_anki != son_baslik:
                    if "DANGER" in ai_karar_ver(su_anki):
                        os.system("rundll32.exe user32.dll,LockWorkStation")
                        os.system("taskkill /F /IM chrome.exe /IM msedge.exe /IM yandex.exe")
                    son_baslik = su_anki
        except: pass
        time.sleep(0.5)

if __name__ == "__main__":
    baslat()