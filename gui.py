from GUI import App
import pickle as pkl

with open('model.pkl', 'rb') as obj:
    model = pkl.load(obj)

if __name__ == '__main__':
    app = App(model)
    app.mainloop()