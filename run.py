#!flask/bin/python

def main():
    """Main launch sequence director.

    Take your protein pills and put your helmet on.
    """
    from app import app
    app.run(debug=True)

main()
