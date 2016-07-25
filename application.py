from flask import Flask, request, render_template
#from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/application-form")
def index_page():
    """Form Page for user input

    serves the template application-form.html at the route
    /application-form. Uses the application-form made in
    skills-html-css which in turn uses the custom styles.skills-html-css
    """


    return render_template("application-form.html")


@app.route("/application")
def application_form():
#def application_form(firstname,lastname,job,salary):

    """Gets first name, last name, salary, and job title from form submission
    """

    form = request.form
    print form

    # firstname = request.args.get("firstname")
    # lastname = request.args.get("lastname")
    # job = request.args.get("job")
    # salary = request.args.get("salary")

    # # salary = request.args.get("salary")

    # print firstname
    # print lastname
    # print job
    # print salary

    # return render_template("application-form.html",
    #                 firstname=firstname,
    #                 lastname=lastname,
    #                 job=job,
    #                 salary=salary)

    # return """
    #         <html>
    #             <body>
    #                 <label for="thank-you-message">
    #                     <p>Thank you {{firstname}} {{lastname}} for applying
    #                     to be a {{job}}. Your minimum salary requirement is 
    #                     {{salary}} dollars."
    #                     </p>
    #                 </label>
    #             </body>
    #         </html>
    #     """

    #****** this one
    # return render_template("./application-response.html",
    #                 firstname=firstname,
    #                 lastname=lastname,
    #                 job=job,
    #                 salary=salary)

    return render_template("./application-response.html",
                    data = form, method = "POST")
# @app.route("/application")
# def application(firstname, lastname, job, salary):
#     """Handles form submission

#     """

#     #call the form file

#     #what about edge cases/failure things?

#     #return thank you message to user
#     return """
#         <html>
#             <body>
#                 <label for="thank-you-message">
#                     <p>Thank you {{firstname}} {{lastname}} for applying
#                     to be a {{job}}. Your minimum salary requirement is 
#                     {{salary}} dollars."
#                     </p>
#                 </label>
#             </body>
#         </html>
            # """

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.run(debug=True)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

