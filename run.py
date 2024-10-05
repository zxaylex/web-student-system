from app import create_app as App


app = App()

if __name__ == "__main__":
    app.run(debug=True)