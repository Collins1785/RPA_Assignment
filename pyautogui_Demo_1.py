#Finding Cricket score - IND Vs ZIM T20 
import pyautogui
import time
import webbrowser

# Step 1: Open Google in browser
webbrowser.open("https://www.google.com")
time.sleep(5)   # wait for browser to load

# Step 2: Click on the Google search bar
# (Google search bar is usually centered; adjust if needed)
pyautogui.click(604, 413)   # You may need to adjust coordinates
time.sleep(1)

# Step 3: Type the search query
pyautogui.write("India vs Zimbabwe T20 World Cup cricket score")
time.sleep(1)

# Step 4: Press Enter to search
pyautogui.press("enter")
time.sleep(5)   # wait for results to load

# Step 5: Click the first search result
# (Coordinates depend on your screen; adjust if needed)
pyautogui.click(400, 600)