## Flask Application Design for KOL Database App

### HTML Files

- **KOL_profile.html**: This HTML file will display the profile of a KOL, including their name, expertise, contact information, and any relevant statistics or metrics.
- **KOL_list.html**: This HTML file will display a list of all KOLs in the database, allowing users to filter and search for specific KOLs based on criteria such as expertise or location.
- **KOL_create.html**: This HTML file will provide a form for users to create new KOL profiles, including personal details, expertise, and any additional relevant information.
- **KOL_edit.html**: This HTML file will provide a form to edit existing KOL profiles, allowing users to update information such as name, expertise, or contact details.

### Routes

- **@app.route('/kol/profile/<int:kol_id>')**: This route will handle requests to view the profile of a specific KOL. It will take the KOL's ID as an argument and retrieve the corresponding data from the database to render the KOL_profile.html page.
- **@app.route('/kol/list')**: This route will handle requests to view the list of all KOLs in the database. It will render the KOL_list.html page and provide a form for filtering and searching.
- **@app.route('/kol/create', methods=['GET', 'POST'])**: This route will handle requests to create new KOL profiles. It will render the KOL_create.html page with a form to input KOL details. Upon form submission (POST request), it will save the data to the database and redirect to the newly created KOL's profile page.
- **@app.route('/kol/edit/<int:kol_id>', methods=['GET', 'POST'])**: This route will handle requests to edit existing KOL profiles. It will take the KOL's ID as an argument, retrieve the corresponding data from the database, and render the KOL_edit.html page. Upon form submission (POST request), it will save the updated data to the database and redirect to the edited KOL's profile page.
- **@app.route('/kol/delete/<int:kol_id>')**: This route will handle requests to delete KOL profiles. It will take the KOL's ID as an argument and delete the corresponding entry from the database. After deletion, it will redirect to the KOL list page.