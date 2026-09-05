import interface
import generator
def generate():
    l = interface.lowercase.get()
    n = interface.numbers.get()
    u = interface.uppercase.get()
    s = interface.symbols.get()
    p = generator.generate_password(l, n, u, s)
    interface.passwordbox.delete(0, "end")
    interface.passwordbox.insert(0, p)
interface.button.config(command=generate)
interface.window.mainloop()
