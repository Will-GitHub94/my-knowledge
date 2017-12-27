# Model View Controller *(Model View Controller)*

The MVC architecture has 3 distinct components:
  - Model
  - View
  - Controller

The aims of MVC are:
  - Code reuse
  - Structured programming
  - Separation of concerns

Below is a description from MSDN on the 3 components of the pattern followed by the author's interpretation:

#### Model

> Model objects are the parts of the application that implement the logic for the application's data domain. Often, model objects retrieve and store model state in a database. For example, a Product object might retrieve information from a database, operate on it, and then write updated information back to a Products table in a SQL Server database.

*The model contains all business logic within the application. As can be seen from the image below, only the controller and the Db interact with the model*

#### View

> Views are the components that display the application's user interface (UI). Typically, this UI is created from the model data. An example would be an edit view of a Products table that displays text boxes, drop-down lists, and check boxes based on the current state of a Product object.

*Views are purely the UI. They are what the user **sees**. Views are driven by the controller*

#### Controller

> Controllers are the components that handle user interaction, work with the model, and ultimately select a view to render that displays UI. In an MVC application, the view only displays information; the controller handles and responds to user input and interaction. For example, the controller handles query-string values, and passes these values to the model, which in turn might use these values to query the database.

*Controllers are the communication link between the model and the views. A controller will take a request from the user (i.e. press a button), process it, and then update the model as need be. Controllers accept sort of HTTP request types (GET, PUT, POST, DELETE...)*


The image below is how the author best interpretted this pattern:

<img src="../assets/mvc.PNG" alt="MVC" style="width: 100px"/><br>

Thoughts:
  - MVC is mainly a client-side architectural pattern (like Angular which is MV*)
  - It really is a true separation of concerns if you are splitting the client into 3 components...
  - What is the amount of business logic held in the model? Will it not be a heavy SPA