import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'szymon.grzybicki@o2.com'
mail.Subject = 'Zapytanie ofertowe'
mail.Body = 'Ile to będzie kosztowało?'
mail.HTMLBody = '<h2>HTML Message body</h2>'

# To attach a file to the email (optional):
zalacznik = "C:\\Users\szymon.grzybicki\Documents\Python Scripts\Wynik.xlsx"
mail.Attachments.Add(zalacznik)

mail.Send()
