from api_app import create_app


app = create_app()

# Run Server
if __name__ == "__main__":
    app.run(debug=True)