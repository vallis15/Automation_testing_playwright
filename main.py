import tkinter as tk
from tkinter import messagebox
from playwright.sync_api import Playwright, sync_playwright


def play_code():
    try:
        with sync_playwright() as playwright:
            run(playwright)
        
        messagebox.showinfo("Test result", "Test went well!") 
    except Exception as e:
        messagebox.showerror("Error", f"Test went not well: {str(e)}")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Přijmout vše").click()
    page.get_by_label("Najít").click()
    page.get_by_label("Najít").fill("sreality")
    page.get_by_label("Hledat Googlem").first.click()
    page.get_by_role("link", name="Sreality.cz • reality a").click()
    page.get_by_role("link", name="m Byty").click()
    page.locator("label").filter(has_text="3+1").click()
    page.locator("label").filter(has_text="4+kk").click()
    page.locator("label").filter(has_text="4+1").click()
    page.locator("tspan").filter(has_text="Moravskoslezský").click()
    page.locator("label").filter(has_text="Ostrava-město").click()
    page.get_by_placeholder("město, městská část, ulice").click()
    page.get_by_placeholder("město, městská část, ulice").fill("muglinov")
    page.get_by_text("městská část Muglinov").click()
    page.get_by_role("button", name="Zobrazit 2 inzeráty").click()
    page.get_by_role("link", name="Prodej bytu 4+kk 124 m²").click()
    page.get_by_label("Váš email").click()
    page.get_by_label("Váš email").fill("vallodemail.cz")
    page.get_by_label("Jméno").click()
    page.get_by_label("Jméno").fill("Daniel")
    page.get_by_label("Telefon").click()
    page.get_by_label("Telefon").fill("Vallo")
    page.get_by_label("", exact=True).click()
    page.get_by_label("", exact=True).fill("Dobrý den, celý den")
    
    page.wait_for_timeout(5000)

    context.close()
    browser.close()

# GUI components
main_window = tk.Tk()
main_window.title("PLAYWRIGHT TESTING")

test_button = tk.Button(main_window, text="TEST SREALITY WEB", command=play_code)
test_button.pack(pady=20)

main_window.mainloop()
