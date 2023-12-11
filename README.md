# AirBnB Clone

This is an open-source project that aims to create a command-line interface (CLI) for managing AirBnB-like objects. It provides a platform for creating and managing objects such as users, places, reviews, amenities, and more.

## Command Interpreter

The command interpreter is the core component of the AirBnB Clone project. It allows users to interact with the application through a command-line interface. Here's how to start and use the command interpreter:

### How to Start the Command Interpreter

1. Clone the repository from GitHub:

   
   git clone https://github.com/your-username/AirBnB_clone.git
   

2. Change into the project directory:

   ````bash
   cd AirBnB_clone
   


3. Run the command interpreter:

   ````bash
   python console.py
   

### How to Use the Command Interpreter

Once the command interpreter is running, you can use various commands to interact with the AirBnB-like objects. Here are some example commands:

- create <class_name> - Create a new object of the specified class.
- show <class_name> <object_id> - Show details of a specific object.
- all - Show all objects.
- update <class_name> <object_id> <attribute_name> <attribute_value> - Update an object's attribute.
- destroy <class_name> <object_id> - Delete an object.

For a complete list of available commands, you can use the help command within the interpreter.

## Examples
Here are some examples of how to use the command interpreter:

1. Creating a new user:

   ````bash
   (AirBnB) create User
   


2. Showing details of a place:

   ````bash
   (AirBnB) show Place 12345
   

3. Updating a user's name:

   ````bash
   (AirBnB) update User 67890 name John Doe
   ```

## Contributors

The following individuals have contributed to the development of this project:

- Natnael Birhanu ([@NathanielBirhanu](https://github.com/NathanielBirhanu))
- Chapa Eresso ([@chapaedb](https://github.com/chapaedb))

We welcome contributions from the community. If you would like to contribute, please fork the repository, make your changes in a branch, and submit a pull request.

## License

This project is licensed under the AlX.
